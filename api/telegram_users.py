import requests


class TelegramUser:

    def __init__(self, first_name, language, telegram_id, last_name=None, username=None):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.language = language
        self.telegram_id = telegram_id

    def create_user(self):
        url = "http://127.0.0.1:8000/api/create-telegram-user"
        data = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'language': self.language,
            'telegram_id': self.telegram_id,
        }
        response = requests.post(url, data=data)
        return response.json()

