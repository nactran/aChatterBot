#coding=utf-8
import os

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

CorpusDir = "data/chinese/conversations.corpus.json"
chat_bot = ChatBot("SillyRobot") # 这里创建了机器人实例，并设定了机器人的名字：SillyRobot
chat_bot.set_trainer(ChatterBotCorpusTrainer)
# 使用中文语料库训练它
chat_bot.train(CorpusDir)
chat_bot.train("chatterbot.corpus.english")
# 开始对话
question = "很高兴认识你"
response = chat_bot.get_response(question)
print(response)
