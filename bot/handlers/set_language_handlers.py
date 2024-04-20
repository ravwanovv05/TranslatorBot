from aiogram import types
from aiogram.utils.exceptions import BadRequest
from api.translate_languages import TranslateLanguage, language_name, language_list
from bot.dispatcher import bot
from bot.inline_buttons.language_buttons import language_button
from math import ceil


async def language_list_handler(message: types.Message):
    text = "Istalgan tilni tanlang."
    await message.answer(text, reply_markup=language_button(1))


async def next_back_language_handler(query: types.CallbackQuery):
    len_languages = len(language_list())
    page = int(query.data.split('_')[-1])

    if query.data.startswith('langnext') and page < ceil(len_languages / 16):
        page += 1
    elif query.data.startswith('langback') and page > 1:
        page -= 1

    try:
        await bot.edit_message_reply_markup(
            query.message.chat.id, query.message.message_id,
            reply_markup=language_button(page)
        )
    except BadRequest:
        await query.answer("Siz allaqachon shu yerdasiz!")


async def delete_language_handler(query: types.CallbackQuery):
    await bot.delete_message(query.from_user.id, query.message.message_id)


async def set_language_handler(query: types.CallbackQuery):
    text = "Til muvafaqqiyatli tanlandi."
    language = int(query.data.split('_')[1])
    telegram_id = query.from_user.id

    translate_language = TranslateLanguage(language, telegram_id)
    translate_language.set_language()

    await bot.delete_message(query.message.chat.id, query.message.message_id)
    await bot.send_message(query.message.chat.id, text)


async def my_selected_language_handler(message: types.Message):
    telegram_id = message.from_user.id
    data = language_name(telegram_id)

    if data['name'] == 'None':
        lang_name = 'Afsuski siz hali tilni sozlamagansiz.'
    else:
        lang_name = data['name']

    await message.answer(f"Sizning tilingiz | {lang_name}")

