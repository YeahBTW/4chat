from chatterbot import ChatBot

fourchatbot = ChatBot('4chat')

imp = input("Start string? ")
out1 = fourchatbot.get_response(imp)
print("bot1: " + str(out1))
out2 = fourchatbot.get_response(out1)
print("bot2: " + str(out2))
while True:
    out1 = fourchatbot.get_response(out2)
    print("bot1: " + str(out1))
    out2 = fourchatbot.get_response(out1)
    print("bot2: " + str(out2))