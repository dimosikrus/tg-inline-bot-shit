import telebot
import re
from telebot import types

token = '69'
bot = telebot.TeleBot(token)

@bot.inline_handler(func=lambda query: len(query.query) > 0)
def query_text(query):
    try:
        r = types.InlineQueryResultArticle(
                id='1',
                title="Абоба \"KitoraBot\"",
                description=query.query,
                input_message_content=types.InputTextMessageContent(
                message_text=query.query)
        )
        bot.answer_inline_query(query.id, [r])
    except Exception as e:
        print(e)
    bot.answer_inline_query(query.id, r)

@bot.inline_handler(func=lambda query: len(query.query) == 0)
def empty_query(query):
    hint = "Введите Chtoto i idite nahyi"
    try:
        r = types.InlineQueryResultArticle(
                id='1',
                title="Бот \"KitoraBot\"",
                description=hint,
                input_message_content=types.InputTextMessageContent(
                message_text="Yeueueueududueueydydysye")
        )
        bot.answer_inline_query(query.id, [r])
    except Exception as e:
        print(e)

#bot.infinity_polling()
