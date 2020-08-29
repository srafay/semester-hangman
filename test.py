import unittest
from main import word_array, guess_word, random_word, player_life


class TestStringMethods(unittest.TestCase):

    def test_words(self):
        # Check if there are words in words array for game to begin
        self.assertNotEqual(word_array, [], "Word array is empty")

    def test_words_are_equal(self):
        # word converted to array and original word should have same length
        self.assertTrue(len(guess_word) == len(random_word), "Length of converted word is of different length")

    def test_initial_player_life(self):
        # Test initial life
        self.assertEqual(player_life, 3, "Player life not equal to 3")


if __name__ == '__main__':
    unittest.main()
