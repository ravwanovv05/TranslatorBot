from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from api.translate_languages import language_list


def language_button(page):
    languages = language_list()
    design, language_name = [], []

    per_page = 16

    start_index = (page - 1) * per_page
    end_index = min(start_index + per_page, len(languages))

    for i in range(start_index, end_index):
        language_name.append(
            InlineKeyboardButton(languages[i]['name'], callback_data=f"lang_{languages[i]['id']}_{page}")

        )

        if len(language_name) == 4:
            design.append(language_name)
            language_name = []

        if len(language_name) < 4 and i == len(languages) - 1:
            design.append(language_name)

    design.append(
        [
            InlineKeyboardButton('⬅ back', callback_data=f"langback_{page}"),
            InlineKeyboardButton('🗑', callback_data='langdel'),
            InlineKeyboardButton('next ➡', callback_data=f"langnext_{page}")
        ]
    )

    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    return ikm
