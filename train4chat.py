from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

fourchatbot = ChatBot('4chat')
trainfc = ChatterBotCorpusTrainer(fourchatbot)

fourchatbot.storage.drop()

trainfc.train("chatterbot.corpus.custom")