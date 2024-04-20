import requests


class TranslateLanguage:
    def __init__(self, language, telegram_id):
        self.language = language
        self.telegram_id = telegram_id

    def set_language(self):
        data = {
            'language': self.language,
            'telegram_id': self.telegram_id,
        }
        url = "http://127.0.0.1:8000/api/set-language"
        response = requests.post(url, data=data)
        return response.json()


def language_list():
    url = "http://127.0.0.1:8000/api/language-list"
    response = requests.get(url)
    return response.json()


def language_name(telegram_id):
    url = f"http://127.0.0.1:8000/api/selected-language/{telegram_id}"
    response = requests.get(url)
    return response.json()


def language_data(telegram_id):
    url = f"http://127.0.0.1:8000/api/language-data/{telegram_id}"
    response = requests.get(url)
    return response.json()
