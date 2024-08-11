"""Translates text into the target language.
Target must be an ISO 639-1 language code.
See https://g.co/cloud/translate/v2/translate-reference#supported_languages
"""

from google.cloud import translate_v2 as translate
translate_client = translate.Client()

idioma_detectado = "pp"
    
def translateUsuario(text: str) -> dict:
    global idioma_detectado
    target = "en"  

    if isinstance(text, bytes):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)

    idioma_detectado = result["detectedSourceLanguage"]

    return print(result.get("translatedText"))


def translateMaquina(text: str) -> dict:
    target = idioma_detectado

    from google.cloud import translate_v2 as translate
    translate_client = translate.Client()

    if isinstance(text, bytes):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)

    return print(result.get("translatedText"))
