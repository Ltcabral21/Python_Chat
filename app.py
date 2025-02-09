import os
from flask import Flask, request, jsonify, send_file
from openai import OpenAI
import requests
from dotenv import load_dotenv
import traceback
import google.generativeai as genai

# Load .env file first
load_dotenv()

app = Flask(__name__)

# Load API keys from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Add validation for API key
if not OPENAI_API_KEY:
    raise ValueError("No OpenAI API key found. Please set OPENAI_API_KEY in .env file")

if not GEMINI_API_KEY:
    raise ValueError("No Gemini API key found. Please set GEMINI_API_KEY in .env file")

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

        required_fields = ['model', 'messages']
        for field in required_fields:
            if field not in data:
                raise APIError(f"Missing required field: {field}", 400)

        model = data.get('model')
        messages = data.get('messages', [])
        user_name = data.get('userName', 'User')

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
                return jsonify({'response': response.choices[0].message.content.strip()})
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
                # Inicializar cliente Gemini
                genai.configure(api_key=GEMINI_API_KEY)
                
                # Formatar o contexto da conversa
                conversation_context = [msg['content'] for msg in messages if msg['role'] != "system"]

                # Preparar o prompt
                prompt = "\n".join(conversation_context)

                # Gerar resposta usando o modelo Gemini
                model = genai.GenerativeModel('gemini-pro')
                response = model.generate_content(
                    prompt,
                    generation_config=genai.types.GenerationConfig(
                        temperature=0.7,
                        top_p=0.8,
                        top_k=40,
                        max_output_tokens=1000,
                    ),
                    safety_settings={
                        "HARM_CATEGORY_HARASSMENT": "BLOCK_MEDIUM_AND_ABOVE",
                        "HARM_CATEGORY_HATE_SPEECH": "BLOCK_MEDIUM_AND_ABOVE"
                    }
                )

                # Verificar se a resposta foi bloqueada
                if response.prompt_feedback and response.prompt_feedback.block_reason:
                    raise APIError(f'Response blocked: {response.prompt_feedback.block_reason}', 400)

                # Imprimir a resposta completa para depuração
                print(f"Resposta completa do Gemini (raw): {response.__dict__}")
                print(f"Resposta do Gemini (texto): {response.text}")

                # Limpar resposta
                response_text = response.text.strip()
                response_text = response_text.replace("assistant", "").strip()

                return jsonify({'response': response_text})

            except genai.types.BlockedPromptException as e:
                raise APIError(f'Prompt blocked: {str(e)}', 400)
            except genai.types.GenerateContentException as e:
                raise APIError(f'Content generation error: {str(e)}', 500)
            except Exception as e:
                traceback.print_exc()
                raise APIError(f'Gemini API error: {str(e)}', 500)
    
    except APIError as api_err:
        return jsonify({'error': api_err.message}), api_err.status_code
    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
