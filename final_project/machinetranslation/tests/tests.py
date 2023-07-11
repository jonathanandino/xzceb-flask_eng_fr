import unittest
# from deep_translator import MyMemoryTranslator
from translator import englishToFrench, frenchToEnglish


class TestTranslation(unittest.TestCase):
    def test_english_to_french_hello(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

    def test_french_to_english_bonjour(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hi")

if __name__ == "__main__":
    unittest.main()