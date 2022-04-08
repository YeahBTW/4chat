from chatterbot import ChatBot

fourchatbot = ChatBot('4chat')

while True:
    imp = input("You: ")
    print("4chat: " + str(fourchatbot.get_response(imp)))