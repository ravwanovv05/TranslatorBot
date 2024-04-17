from aiogram import types

from api.translators import Translator


async def translate_message_handler(message: types.Message):
    telegram_id = message.from_user.id
    text = message.text
    translator = Translator(text, telegram_id)
    translate = translator.translate()
    if translate:
        translated_text = translate['translated_text']

        await message.answer(translated_text)
    else:
        await message.answer("Siz til tanlamagansiz tilni tanlash uchun esa /set buyrug'ini yuboring.")
