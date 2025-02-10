# 📌 Chat AI Interface

Chat web which combines GPT-4o-Mini and  Gemini Flash for awesome and versatile conversations!



---

## 🚀 Quick Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Ltcabral21/Python_Chat.git
cd Python_Chat
```

### 2️⃣ Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies
```bash
pip install Flask openai requests python-dotenv google-generativeai


```

### 4️⃣ Configure environment variables
Create a `.env` file in the project root and add your API keys:
```env
OPENAI_API_KEY=your-key-here
GEMINI_API_KEY=your-key-here
```

### 5️⃣ Run the Flask server
```bash
python app.py
```

### 6️⃣ Access in your browser
Open [`http://localhost:5000`](http://localhost:5000) to use the chat interface.

---

## 🛠 Technologies Used

- **Frontend:** HTML, JavaScript (vanilla), Tailwind CSS
- **Backend:** Python (Flask)
- **APIs:** OpenAI GPT-4o-mini, Google Gemini

---

## ✨ Features

✅ Modern and responsive chat interface<br>
✅ Support for multiple AI models (GPT-4o-mini Turbo and Gemini Flash)<br>
✅ Dynamic model switching during conversations<br>
✅ Persistent message history in the browser<br>
✅ Robust error handling for API failures<br>
✅ Clean and well-documented code

---

## 📁 Project Structure

```
chat-ai-interface/
│── static/
│   ├── styles.css         # CSS styles (Tailwind CSS)
│   ├── app.js             # Frontend logic in JavaScript
│── templates/
│   ├── index.html         # Chat interface
│── .env                   # Environment variables file (API Keys)
│── app.py                 # Flask server (backend)
│── requirements.txt       # Project dependencies
│── README.md              # Project documentation
```

---

## ⚡ How to Contribute

1️⃣ **Fork** the project<br>
2️⃣ Create a **branch** (`git checkout -b my-feature`)<br>
3️⃣ **Commit** your changes (`git commit -m 'Add new feature'`)<br>
4️⃣ **Push** to the branch (`git push origin my-feature`)<br>
5️⃣ Open a **Pull Request** 🚀

---

📌 Developed with ❤️ by Lucas Cabral

# AI-Chat
