document.addEventListener('DOMContentLoaded', () => {
    let selectedModel = localStorage.getItem('selectedModel') || 'gpt-4o-mini';
    let userName = localStorage.getItem('userName');
    let chatHistory = [];
    let conversationHistory = [];

    const sendBtn = document.getElementById('send-btn');
    const model1Btn = document.getElementById('model-1');
    const model2Btn = document.getElementById('model-2');
    const userInput = document.getElementById('user-input');
    const chatHistoryElement = document.getElementById('chat-history');

    // Solicitar nome do usuário se não existir
    if (!userName) {
        userName = prompt('Por favor, digite seu nome:') || 'User';
        localStorage.setItem('userName', userName);
    }

    // Carregar estado inicial
    loadInitialState();

    sendBtn.addEventListener('click', sendMessage);
    model1Btn.addEventListener('click', () => switchModel('gpt-4o-mini'));
    model2Btn.addEventListener('click', () => switchModel('gemini-2.0-flash'));

    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    function sendMessage() {
        const userMessage = userInput.value;
        if (userMessage.trim() === "") return;

        chatHistory.push({ sender: 'user', message: userMessage });
        conversationHistory.push({ role: "user", content: userMessage });
        
        // Salvar no localStorage
        localStorage.setItem('chatHistory', JSON.stringify(chatHistory));
        localStorage.setItem('conversationHistory', JSON.stringify(conversationHistory));
        
        displayChatHistory();

        fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 
                model: selectedModel, 
                messages: conversationHistory,
                userName: userName
            }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                throw new Error(data.error);
            }
            chatHistory.push({ sender: 'bot', message: data.response });
            conversationHistory.push({ role: "assistant", content: data.response });
            
            // Salvar no localStorage após resposta
            localStorage.setItem('chatHistory', JSON.stringify(chatHistory));
            localStorage.setItem('conversationHistory', JSON.stringify(conversationHistory));
            
            displayChatHistory();
        })
        .catch(error => {
            console.error('Error:', error);
            chatHistory.push({ 
                sender: 'bot', 
                message: `Error: ${error.message || 'Could not get response'}`
            });
            displayChatHistory();
        });

        userInput.value = "";
    }

    function switchModel(model) {
        selectedModel = model;
        localStorage.setItem('selectedModel', model);
        
        model1Btn.classList.toggle('ring-2', model === 'gpt-4o-mini');
        model2Btn.classList.toggle('ring-2', model === 'gemini-2.0-flash');
        
        chatHistory = [];
        conversationHistory = [];

        localStorage.setItem('chatHistory', JSON.stringify(chatHistory));
        localStorage.setItem('conversationHistory', JSON.stringify(conversationHistory));
        
        displayChatHistory();
    }

    function loadInitialState() {
        // Carregar histórico do localStorage
        chatHistory = JSON.parse(localStorage.getItem('chatHistory') || '[]');
        conversationHistory = JSON.parse(localStorage.getItem('conversationHistory') || '[]');

        // Se não houver histórico, apenas adicionar o contexto do sistema
        if (conversationHistory.length === 0) {
            conversationHistory.push({
                role: "system",
                content: `You are a helpful AI assistant talking to ${userName}. Remember their name and previous context.`
            });
            
            localStorage.setItem('conversationHistory', JSON.stringify(conversationHistory));
        }

        displayChatHistory();
    }

    function displayChatHistory() {
        chatHistoryElement.innerHTML = chatHistory.map(entry => {
            const messageClass = entry.sender === 'user' ? 'user-message' : 'bot-message';
            return `
                <div class="chat-message ${messageClass}">
                    <div class="text-sm text-gray-600 mb-1">${entry.sender === 'user' ? 'You' : 'AI'}</div>
                    <div>${entry.message}</div>
                </div>
            `;
        }).join('');
        chatHistoryElement.scrollTop = chatHistoryElement.scrollHeight;
    }
});
