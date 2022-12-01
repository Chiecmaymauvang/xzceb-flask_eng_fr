import unittest
from trasnslator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """ 
    Class to test the function english_to_french
    """
    def test1(self):
        """ 
        Function to test the function english_to_french
        """
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Bonjour"), "Hello")

class TestFrenchToEnglish(unittest.TestCase):
    """ This class is for unit testing french_to_english """
    def tests_1(self):
        """ tests for french_to_english """
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertIsNotNone(french_to_english(" "), "Value can not be None")

unittest.main()