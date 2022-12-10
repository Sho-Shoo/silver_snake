from WordList import *
import unittest


class TestClass(unittest.TestCase):

    def test_adding_word(self):
        wordlist = WordList()
        wordlist.add('ha')
        self.assertEqual(wordlist.list[-1], 'ha')

    def test_generate_swear_word_dict(self):
        word_list = WordList()
        print(word_list)
        # test by yourself :)


if __name__ == '__main__':
    unittest.main()
