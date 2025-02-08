import os
from flask import Flask, request, jsonify, send_file
from openai import OpenAI
import requests
from dotenv import load_dotenv
from typing import Optional, Dict, Any
import traceback

# Load .env file first
load_dotenv()

app = Flask(__name__)

# Load API keys from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Add validation for API key
if not OPENAI_API_KEY:
    raise ValueError("No OpenAI API key found. Please set OPENAI_API_KEY in .env file")

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

class APIError(Exception):
    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

@app.route('/')
def home():
    return send_file('index.html')

@app.route('/app.js')
def serve_js():
    return send_file('app.js')

@app.errorhandler(APIError)
def handle_api_error(error):
    return jsonify({'error': error.message}), error.status_code

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        # Validar request
        if not request.is_json:
            raise APIError("Content-Type must be application/json", 400)

        data = request.json
        if not isinstance(data, dict):
            raise APIError("Invalid request format", 400)

        # Validar campos obrigatórios
        required_fields = ['model', 'messages']
        for field in required_fields:
            if field not in data:
                raise APIError(f"Missing required field: {field}", 400)

        model = data.get('model')
        messages = data.get('messages', [])
        user_name = data.get('userName', 'User')

        # Validar chaves API
        if not OPENAI_API_KEY or not GEMINI_API_KEY:
            raise APIError('API keys not configured', 500)

        # Validar modelo
        if model not in ['gpt-4o-mini', 'gemini-2.0-flash']:
            raise APIError('Invalid model specified', 400)

        # Validar mensagens
        if not isinstance(messages, list) or not messages:
            raise APIError('Invalid or empty messages array', 400)

        if model == 'gpt-4o-mini':
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini-2024-07-18",
                    messages=messages,
                    timeout=30
                )
                return jsonify({'response': response.choices[0].message.content})
            except Exception as e:
                error_message = str(e)
                if 'rate limit' in error_message.lower():
                    raise APIError('OpenAI rate limit exceeded. Please try again later.', 429)
                elif 'invalid api key' in error_message.lower():
                    raise APIError('Invalid OpenAI API key', 401)
                else:
                    raise APIError(f'OpenAI API error: {error_message}', 500)

        elif model == 'gemini-2.0-flash':
            try:
                formatted_conversation = f"""You are an AI assistant.
You must remember all context from the conversation and previous messages.
Here's the conversation history:

"""
                for msg in messages:
                    if msg['role'] == "system":
                        continue
                    role = user_name if msg['role'] == "user" else "Assistant"
                    formatted_conversation += f"{role}: {msg['content']}\n"

                formatted_conversation += f"\n Keep the conversation context in mind.\nAssistant: "
                
                url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
                headers = {"Content-Type": "application/json"}
                params = {"key": GEMINI_API_KEY}
                payload = {
                    "contents": [{
                        "parts": [{
                            "text": formatted_conversation
                        }]
                    }]
                }

                response = requests.post(
                    url, 
                    headers=headers, 
                    params=params, 
                    json=payload,
                    timeout=30  # timeout em segundos
                )

                if response.status_code != 200:
                    error_data = response.json()
                    error_message = error_data.get('error', {}).get('message', 'Unknown error')
                    raise APIError(f'Gemini API error: {error_message}', response.status_code)

                response_json = response.json()
                
                if 'candidates' in response_json:
                    return jsonify({'response': response_json['candidates'][0]['content']['parts'][0]['text']})
                else:
                    raise APIError('Unexpected Gemini response format', 500)
                    
            except requests.Timeout:
                raise APIError('Gemini API timeout', 504)
            except requests.RequestException as e:
                raise APIError(f'Gemini API connection error: {str(e)}', 503)
            except Exception as e:
                raise APIError(f'Gemini API error: {str(e)}', 500)

    except APIError:
        raise
    except Exception as e:
        traceback.print_exc()  # Log the full error
        raise APIError(f'Server error: {str(e)}', 500)

if __name__ == '__main__':
    app.run(debug=True)
