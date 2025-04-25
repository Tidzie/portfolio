// DOM Elements
const chatBody = document.querySelector('.chat-body');
const messageInput = document.querySelector('.message-input');
const sendButton = document.querySelector('.chat-controls button:last-child');

// Function to create message elements
const createMessageElement = (content, classes) => {
    const div = document.createElement('div');
    div.classList.add('message', classes);
    div.innerHTML = `<div class="message-text">${content}</div>`;
    return div;
};

// Function to handle outgoing messages
const handleOutgoingMessage = (userMessage) => {
    // Create and append user message
    const userMessageElement = createMessageElement(userMessage, 'user-message');
    chatBody.appendChild(userMessageElement);
    
    // Get bot response
    const botResponse = findAnswer(userMessage);
    
    // Create and append bot message
    setTimeout(() => {
        const botMessageElement = createMessageElement(botResponse, 'bot-message');
        chatBody.appendChild(botMessageElement);
        chatBody.scrollTop = chatBody.scrollHeight;
    }, 500);
    
    // Clear input
    messageInput.value = '';
};

// Handle form submission
document.querySelector('.chat-form').addEventListener('submit', (e) => {
    e.preventDefault();
    const userMessage = messageInput.value.trim();
    if (userMessage) {
        handleOutgoingMessage(userMessage);
    }
});

// Handle Enter key press
messageInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        const userMessage = messageInput.value.trim();
        if (userMessage) {
            handleOutgoingMessage(userMessage);
        }
    }
});

// Handle send button click
sendButton.addEventListener('click', () => {
    const userMessage = messageInput.value.trim();
    if (userMessage) {
        handleOutgoingMessage(userMessage);
    }
});