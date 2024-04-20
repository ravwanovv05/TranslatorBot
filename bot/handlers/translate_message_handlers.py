from aiogram import types
from api.translate_languages import language_data
from translate_FUN.translator import translate_message


async def translate_message_handler(message: types.Message):
    telegram_id = message.from_user.id
    text = message.text
    data = language_data(telegram_id)
    translator = translate_message(text, data['lang_code'])

    if translator:
        await message.answer(translator)
    else:
        await message.answer("Siz til tanlamagansiz tilni tanlash uchun esa /set buyrug'ini yuboring.")
