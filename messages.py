def show_messages(lst: list):
    for message in lst:
        print(message)


def send_messages(msg_to_send, sent_messages):
    while msg_to_send:
        msg = msg_to_send.pop()
        print(msg)
        sent_messages.append(msg)


messages = [
    "Hello!",
    "How are you?",
    "Nice to meet you.",
    "Have a great day!",
    "Goodbye!",
    "What's up?",
    "Take care!",
    "See you later.",
    "Enjoy your day!",
    "Keep smiling!"
]
list_to_fill = []
show_messages(messages)

send_messages(messages.copy(), list_to_fill)
print("messages:", messages, "\nList to fill:", list_to_fill)
