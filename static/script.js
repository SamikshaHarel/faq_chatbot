function getResponse() {
    const userInput = document.getElementById('user_input').value;
    const chatbox = document.getElementById('chatbox');

    if (!userInput.trim()) {
        alert("Please type your question.");
        return;
    }

    // Display user's question in the chatbox
    const userMessageDiv = document.createElement('div');
    userMessageDiv.classList.add('user-message');
    userMessageDiv.textContent = userInput;
    chatbox.appendChild(userMessageDiv);

    // Clear the textarea
    document.getElementById('user_input').value = '';

    // Scroll to the bottom of the chatbox
    chatbox.scrollTop = chatbox.scrollHeight;

    // Send the user input to Flask for processing
    fetch('/get_response', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 'user_input': userInput })
    })
    .then(response => response.json())
    .then(data => {
        // Display bot's response in the chatbox
        const botResponseDiv = document.createElement('div');
        botResponseDiv.classList.add('bot-response');
        botResponseDiv.textContent = data.response;
        chatbox.appendChild(botResponseDiv);

        // Scroll to the bottom of the chatbox
        chatbox.scrollTop = chatbox.scrollHeight;
    })
    .catch(error => {
        const errorDiv = document.createElement('div');
        errorDiv.classList.add('bot-response');
        errorDiv.textContent = "Sorry, something went wrong. Please try again.";
        chatbox.appendChild(errorDiv);
        chatbox.scrollTop = chatbox.scrollHeight;
    });
}
