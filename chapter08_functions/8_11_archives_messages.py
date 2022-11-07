

messages = ['hello world', 'i love python', 'test message', 'wtf']
sent_messages= []

def print_messages(messages, sent_messages):
    while messages:
        sent_message = messages.pop(0)
        sent_messages.append(sent_message)

print_messages(messages[:], sent_messages)
print(messages)
print(sent_messages)