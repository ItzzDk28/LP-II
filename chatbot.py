# Predefined dictionary for chatbot responses
responses = {
    "hello": "Hello! How can I assist you today?",
    "hi": "Hi there! How can I help?",
    "hey": "Hey! What can I do for you?",
    "products": "We offer a variety of products. How can I assist you with a specific product?",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're welcome! If you have any more questions, feel free to ask."
}

def chatbot_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()
    
    # Check if the user input matches any predefined keywords
    for keyword in responses:
        if keyword in user_input:
            return responses[keyword]
    
    # If no keyword is matched, provide a default response
    return "I'm sorry, I don't understand. Can you please rephrase your question?"

# Main loop for chatbot interaction
print("Chatbot: Hello! How can I assist you today? (Type 'bye' to exit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot:", responses["bye"])
        break
    else:
        response = chatbot_response(user_input)
        print("Chatbot:", response)
