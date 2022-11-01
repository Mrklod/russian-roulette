from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters
#import numexpr

"""expr = input("Введите пример: ")

resultat = numexpr.evaluate(expr)

print(resultat)"""

TG_TOKEN = "5668214541:AAFoa7JzrDib1aD0SM0C2al4J_GsxK6gbYU"

def message_handler(bot: Bot,update: Update):
    return 

def main():
    bot = Bot(
        token=TG_TOKEN,
    )
    updater = Updater(
        bot=bot,
    )