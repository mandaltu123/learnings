import unittest
import capitalize_string


class TestCapitalizedString(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = capitalize_string.cap_test(text)
        self.assertEqual(result, 'Python')

    def test_two_multiple(self):
        text = 'python test'
        result = capitalize_string.cap_test(text)
        self.assertEqual(result, 'Python test')


if __name__ == '__main__':
    unittest.main()
