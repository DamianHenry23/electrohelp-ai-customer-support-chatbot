
// =====================================
// ELECTROHELP AI - CHAT FUNCTIONALITY
// WITH CONVERSATION MEMORY
// =====================================

// Get HTML elements
const chatForm = document.getElementById("chatForm");
const userInput = document.getElementById("userInput");
const chatMessages = document.getElementById("chatMessages");
const sendButton = document.getElementById("sendButton");

// API endpoint
const API_URL = "/chat";

// Store conversation history
let conversationHistory = [];

// =====================================
// DISPLAY CHAT MESSAGES
// =====================================

function addMessage(message, sender) {

    const messageElement = document.createElement("div");

    messageElement.classList.add("message");

    if (sender === "user") {
        messageElement.classList.add("user-message");
    } else {
        messageElement.classList.add("ai-message");
    }

    messageElement.textContent = message;

    chatMessages.appendChild(messageElement);

    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// =====================================
// DISPLAY TYPING INDICATOR
// =====================================

function showTypingIndicator() {

    const typingElement = document.createElement("div");

    typingElement.classList.add("typing");
    typingElement.id = "typingIndicator";

    typingElement.textContent = "ElectroHelp AI is thinking...";

    chatMessages.appendChild(typingElement);

    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// =====================================
// REMOVE TYPING INDICATOR
// =====================================

function removeTypingIndicator() {

    const typingElement = document.getElementById("typingIndicator");

    if (typingElement) {
        typingElement.remove();
    }
}

// =====================================
// SEND MESSAGE TO FASTAPI
// =====================================

async function sendMessage(message) {

    const cleanedMessage = message.trim();

    if (!cleanedMessage || sendButton.disabled) {
        return;
    }

    // Display customer message
    addMessage(cleanedMessage, "user");

    // Clear input
    userInput.value = "";

    // Disable send button
    sendButton.disabled = true;

    // Show typing indicator
    showTypingIndicator();

    try {

        // Send current message and previous history
        const response = await fetch(API_URL, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: cleanedMessage,
                history: conversationHistory
            })

        });

        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        const data = await response.json();

        // Remove typing indicator
        removeTypingIndicator();

        // Display AI response
        addMessage(data.ai_response, "ai");

        // Save customer message
        conversationHistory.push({
            role: "user",
            content: cleanedMessage
        });

        // Save AI response
        conversationHistory.push({
            role: "assistant",
            content: data.ai_response
        });

        // Keep only the latest 20 messages
        conversationHistory = conversationHistory.slice(-20);

    } catch (error) {

        console.error("Chat error:", error);

        removeTypingIndicator();

        addMessage(
            "Sorry, I'm having trouble connecting right now. Please try again.",
            "ai"
        );

    } finally {

        sendButton.disabled = false;

        userInput.focus();
    }
}

// =====================================
// HANDLE FORM SUBMISSION
// =====================================

chatForm.addEventListener("submit", function(event) {

    event.preventDefault();

    sendMessage(userInput.value);

});

// =====================================
// SUGGESTED QUESTION BUTTONS
// =====================================

function sendSuggestion(message) {

    sendMessage(message);

}
