import random
from datetime import datetime


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
            "I can chat, tell you the time and date, "
            "remember your name during this session, "
            "and perform simple calculations."
        ],
        "I'm fine": [
            "That's great to hear!",
            "Glad to know you're doing well!"
        ],
    }

    print("\n🤖 PyBot: Hello! I am PyBot.")
    print("🤖 PyBot: Type 'help' to see commands.")
    print("🤖 PyBot: Type 'bye' to exit.\n")

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
6. time
7. date
8. calculate 10 + 5
9. tell me a joke
10. thank you
11. what can you do
12. bye / exit / quit
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

        elif user_input == "time":
            current_time = datetime.now().strftime("%I:%M:%S %p")
            print(f"PyBot: The current time is {current_time}.")

        elif user_input == "date":
            current_date = datetime.now().strftime("%d-%m-%Y")
            print(f"PyBot: Today's date is {current_date}.")

        elif user_input.startswith("calculate "):
            expression = user_input[len("calculate "):].split()

            if len(expression) != 3:
                print("PyBot: Example: calculate 10 + 5")
                continue

            try:
                num1 = float(expression[0])
                operator = expression[1]
                num2 = float(expression[2])

                if operator == "+":
                    result = num1 + num2
                elif operator == "-":
                    result = num1 - num2
                elif operator == "*":
                    result = num1 * num2
                elif operator == "/":
                    if num2 == 0:
                        print("PyBot: Cannot divide by zero.")
                        continue
                    result = num1 / num2
                else:
                    print("PyBot: Supported operators: +, -, *, /")
                    continue

                print(f"PyBot: Result = {result:g}")

            except ValueError:
                print("PyBot: Please enter valid numbers.")

        elif user_input == "tell me a joke":
            jokes = [
                "Why do programmers prefer dark mode? "
                "Because light attracts bugs!",
                "Why did the Python programmer wear glasses? "
                "Because they couldn't C!",
                "Why was the computer cold? "
                "It left its Windows open!"
            ]
            print("PyBot:", random.choice(jokes))

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