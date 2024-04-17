import requests


class Translator:
    def __init__(self, text: str, telegram_id: int):
        self.text = text
        self.telegram_id = telegram_id

    def translate(self):
        url = f"http://127.0.0.1:8000/api/translate-message"
        data = {
            'text': self.text,
            'telegram_id': self.telegram_id
        }
        response = requests.post(url, data=data)

        return response.json()
