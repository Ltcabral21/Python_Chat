# 📌 Chat AI Interface

Uma interface de chat moderna que integra **OpenAI GPT-3.5 Turbo** e **Google Gemini** em uma única aplicação web, permitindo conversas inteligentes e interativas com múltiplos modelos de IA.

---

## 🚀 Configuração Rápida

### 1️⃣ Clone o repositório e instale as dependências
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/chat-ai-interface.git
cd chat-ai-interface

# Crie e ative um ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

### 2️⃣ Configure as variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto e adicione suas chaves de API:
```env
OPENAI_API_KEY=sua-chave-aqui
GEMINI_API_KEY=sua-chave-aqui
```

### 3️⃣ Execute o servidor Flask
```bash
python app.py
```

### 4️⃣ Acesse no navegador
Abra [`http://localhost:5000`](http://localhost:5000) para usar a interface de chat.

---

## 🛠 Tecnologias Utilizadas

- **Frontend:** HTML, JavaScript (vanilla), Tailwind CSS
- **Backend:** Python (Flask)
- **APIs:** OpenAI GPT-3.5, Google Gemini

---

## ✨ Funcionalidades

✅ Interface de chat moderna e responsiva<br>
✅ Suporte a múltiplos modelos de IA (GPT-3.5 Turbo e Gemini)<br>
✅ Alternância dinâmica entre modelos durante a conversa<br>
✅ Histórico de mensagens persistente no navegador<br>
✅ Tratamento de erros robusto para falhas de API<br>
✅ Código limpo e bem documentado

---

## 📁 Estrutura do Projeto

```
chat-ai-interface/
│── static/
│   ├── styles.css         # Estilos CSS (Tailwind CSS)
│   ├── app.js             # Lógica do frontend em JavaScript
│── templates/
│   ├── index.html         # Interface do chat
│── .env                   # Arquivo de variáveis de ambiente (API Keys)
│── app.py                 # Servidor Flask (backend)
│── requirements.txt       # Dependências do projeto
│── README.md              # Documentação do projeto
```

---

## ⚡ Como Contribuir

1️⃣ Faça um **fork** do projeto<br>
2️⃣ Crie uma **branch** (`git checkout -b minha-feature`)<br>
3️⃣ **Commit** suas alterações (`git commit -m 'Adiciona nova funcionalidade'`)<br>
4️⃣ Faça um **push** para a branch (`git push origin minha-feature`)<br>
5️⃣ Abra um **Pull Request** 🚀

---

## 📜 Licença

Este projeto está licenciado sob a **MIT License** - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

📌 Desenvolvido com ❤️ por [Seu Nome](https://github.com/seu-usuario)

