import unittest
from unittest import mock
from src.utils.utils import addValues, confirm_user_choice


class TestConfirmUserChoice(unittest.TestCase):
    def test_yes(self):
        result = confirm_user_choice("y", ["y"])
        self.assertTrue(result)

    def test_eventual_yes(self):
        result = confirm_user_choice("y", ["apple", "pear", "y"])
        self.assertTrue(result)

    def test_no(self):
        result = confirm_user_choice("y", ["n"])
        self.assertFalse(result)

    def test_no_valid_input(self):
        with self.assertRaises(ValueError):
            confirm_user_choice(None, ["tree"])


class TestAdd(unittest.TestCase):
    def test_add(self):
        result = addValues(2, 5)
        self.assertEqual(result, 7)


# if __name__ == "__main__":
#     unittest.main()

# from io import StringIO
# @mock.patch("sys.stdout", new_callable=StringIO)
# def main_op(self, tst_str, mock_stdout):
#     with mock.patch("builtins.input", side_effect=tst_str):
#         confirm_user_choice("y")
#     return mock_stdout.getvalue()

# from src.helpers import index
# from src.helpers.index import *
# python -m unittest test_utils.py
# python -m unittest discover tests
