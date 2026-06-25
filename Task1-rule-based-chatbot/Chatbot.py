def chatbot():
    print("Chatbot: Hello! I'm your assistant. Type 'quit' to exit.")

    while True:
        user_input = input("You: ").lower().strip()

        # Greetings
        if user_input in ["hi", "hello", "hey"]:
            print("Chatbot: Hello! How can I help you today?")

        # Farewells
        elif user_input in ["bye", "goodbye", "see you"]:
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Common Questions
        elif "your name" in user_input:
            print("Chatbot: I'm RuleBot, your simple assistant!")

        elif "how are you" in user_input:
            print("Chatbot: I'm doing great, thank you for asking!")

        elif "what can you do" in user_input:
            print("Chatbot: I can answer basic questions and have simple conversations!")

        elif "time" in user_input:
            import datetime
            print(f"Chatbot: Current time is {datetime.datetime.now().strftime('%H:%M')}")

        elif "help" in user_input:
            print("Chatbot: You can ask me: my name, how I am, what I can do, or the time!")

        elif user_input == "quit":
            print("Chatbot: Bye! See you soon!")
            break

        # Default
        else:
            print("Chatbot: Sorry, I didn't understand that. Type 'help' to see what I can do.")

# Start the chatbot
chatbot()
