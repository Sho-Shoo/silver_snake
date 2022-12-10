from Text import *
import unittest


class TestClass(unittest.TestCase):

    def test_analysis_is_correct(self):
        text1 = Text("The Ass of my aSs is not my arse")
        result1 = text1.generate_analysis()
        self.assertEqual(result1['ass']['position'], [1, 4])
        self.assertEqual(result1['ass']['count'], 2)
        self.assertEqual(result1['arse']['position'], [8])
        self.assertEqual(result1['arse']['count'], 1)




if __name__ == '__main__':
    unittest.main()
