from googletrans import Translator


def translate_message(text: str, dest: str):
    translator = Translator(service_urls=['translate.google.com', 'translate.google.co.kr'])

    translated = translator.translate(text, dest=dest)
    return translated.text

