import random


def chatbot():
    user_name = ""

    responses = {
        "hello": [
            "Hello! How can I help you?",
            "Hi there! Nice to meet you!",
            "Hey! What's up?"
        ],
        "hi": [
            "Hi! How are you?",
            "Hello! What can I do for you?"
        ],
        "how are you": [
            "I'm fine, thanks!",
            "I'm doing great! How about you?"
        ],
        "what is your name": [
            "I'm PyBot, your Python chatbot!"
        ],
        "thank you": [
            "You're welcome!",
            "Happy to help!"
        ],
        "who created you": [
            "I was created using Python."
        ],
        "what can you do": [
            "I can chat with you and remember your name during this session."
        ],
        "i'm fine": [
            "That's great to hear!",
            "Glad to know you're doing well!"
        ],
    }

    print("\nPyBot: Hello! I am PyBot.")
    print("PyBot: Type 'help' to see commands.")
    print("PyBot: Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").strip().lower()

        if not user_input:
            print("PyBot: Please enter something.")
            continue

        if user_input in ("bye", "exit", "quit"):
            print(f"PyBot: Goodbye {user_name or 'friend'}! Have a nice day!")
            break

        elif user_input == "help":
            print("""
PyBot commands:
1. hello / hi
2. how are you
3. what is your name
4. my name is <your name>
5. what is my name
6. thank you
7. what can you do
8. bye / exit / quit
""")

        elif user_input.startswith("my name is "):
            user_name = user_input[len("my name is "):].strip().title()

            if user_name:
                print(f"PyBot: Nice to meet you, {user_name}!")
            else:
                print("PyBot: Please tell me your name.")

        elif user_input == "what is my name":
            if user_name:
                print(f"PyBot: Your name is {user_name}.")
            else:
                print("PyBot: You haven't told me your name yet.")

        else:
            matched = False

            for phrase, replies in responses.items():
                if phrase in user_input:
                    print("PyBot:", random.choice(replies))
                    matched = True
                    break

            if not matched:
                print(
                    "PyBot: Sorry, I don't understand that. "
                    "Type 'help' to see what I can do."
                )


if __name__ == "__main__":
    chatbot()