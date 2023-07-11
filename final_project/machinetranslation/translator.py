import json
import os

from deep_translator import MyMemoryTranslator


def englishToFrench(englishText):
    """
    translate English to French
    """
    translator = MyMemoryTranslator(source='en-US', target='fr-FR')
    frenchText = translator.translate(englishText)
    return frenchText

def frenchToEnglish(frenchText):
    """
    Translate French text to English.
    """
    translator = MyMemoryTranslator(source='fr-FR', target='en-US')
    englishText = translator.translate(frenchText)
    return englishText