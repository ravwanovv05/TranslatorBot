import logging
from aiogram import types
from aiogram.types import InlineKeyboardButton, WebAppInfo, InlineKeyboardMarkup
from aiogram.utils.executor import start_webhook
from bot.dispatcher import dp
from bot.handlers.main_handlers import start_handler, help_handler
from bot.handlers.set_language_handlers import (
    language_list_handler, next_back_language_handler, set_language_handler,
    my_selected_language_handler, delete_language_handler)
from bot.handlers.translate_message_handlers import translate_message_handler
from bot.handlers.main_handlers import WEBHOOK_URL_PATH, on_startup, on_shutdown, WEBAPP_HOST, WEBAPP_PORT


dp.register_message_handler(start_handler, commands=['start'])
dp.register_message_handler(help_handler, lambda message: message.text == 'Yordam 🆘')


@dp.message_handler(commands=['instagram'])
async def start_handler(message: types.Message):

    design = [
        [InlineKeyboardButton("Instagram", web_app=WebAppInfo(url="https://www.instagram.com/"))]
    ]

    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    await message.answer("Instagram", reply_markup=ikm)


dp.register_message_handler(language_list_handler, lambda message: message.text == 'Tilni sozlash 🌐')
dp.register_callback_query_handler(next_back_language_handler, lambda query: query.data.startswith(('langnext', 'langback')))
dp.register_callback_query_handler(delete_language_handler, lambda query: query.data.startswith('langdel'))
dp.register_callback_query_handler(set_language_handler, lambda query: query.data.startswith('lang'))
dp.register_message_handler(my_selected_language_handler, lambda message: message.text == 'Mening tilim 👁‍🗨')
dp.register_message_handler(translate_message_handler)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_URL_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
