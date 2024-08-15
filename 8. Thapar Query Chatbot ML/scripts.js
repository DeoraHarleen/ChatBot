// scripts.js
document.getElementById('send-button').addEventListener('click', function() {
    const userInput = document.getElementById('user-input').value;
    if (userInput) {
        const chatBox = document.getElementById('chat-box');
        chatBox.innerHTML += `<div class="user-message">${userInput}</div>`;
        document.getElementById('user-input').value = '';

        // Send message to backend
        fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            // body: JSON.stringify({ inputs: [userInput] })
            body: JSON.stringify({"inputs": [/* your input data here */]})
        })
        .then(response => response.json())
        .then(data => {
            chatBox.innerHTML += `<div class="bot-response">${data.prediction}</div>`;
            chatBox.scrollTop = chatBox.scrollHeight;
        });
    }
});
