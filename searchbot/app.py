from telebot import types, TeleBot

from searchbot.config import load_config
from searchbot.handlers import register_handlers

def init_app():
    config = load_config()
    bot = TeleBot(config['token'])
    register_handlers(bot, config)
    bot.polling()
