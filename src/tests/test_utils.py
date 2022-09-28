import unittest
from unittest import mock
from src.utils.utils import addValues, confirm_user_choice, set_user_name


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


class TestSetUserName(unittest.TestCase):
    # doesn't test str print output console.
    def test_set_user_name(self):
        with mock.patch("builtins.input", return_value="Tim"):
            result = set_user_name()
        self.assertEqual(result, "Tim")


# i have no idea how to write a test for this util.
# class TestSetUserClass(unittest.TestCase):
#     def test_set_user_class(self):


# from src.helpers import index
# from src.helpers.index import *
# python -m unittest test_utils.py
# python -m unittest discover tests
