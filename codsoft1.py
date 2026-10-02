print("AI Chatbot")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user in ["hello", "hi", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif "how are you" in user:
        print("Bot: I am fine. Thank you for asking!")

    elif "your name" in user:
        print("Bot: I am a Rule-Based AI Chatbot.")

    elif "what is ai" in user:
        print("Bot: AI stands for Artificial Intelligence. It enables machines to perform intelligent tasks.")

    elif "python" in user:
        print("Bot: Python is a popular programming language used in AI, ML and software development.")

    elif "thank" in user:
        print("Bot: You're welcome!")

    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a nice day")
        break

    else:
        print("Bot: Sorry, I don't understand that question.")