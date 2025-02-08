# 📌 Chat AI Interface

A modern chat interface that integrates **OpenAI GPT-3.5 Turbo** and **Google Gemini** into a single web application, enabling intelligent and interactive conversations with multiple AI models.

---

## 🚀 Quick Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/chat-ai-interface.git
cd chat-ai-interface
```

### 2️⃣ Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
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
- **APIs:** OpenAI GPT-3.5, Google Gemini

---

## ✨ Features

✅ Modern and responsive chat interface<br>
✅ Support for multiple AI models (GPT-3.5 Turbo and Gemini)<br>
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

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

📌 Developed with ❤️ by [Your Name](https://github.com/your-username)

