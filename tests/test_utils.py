import unittest

# from src.helpers import index
# from src.helpers.index import *
from src.utils.utils import addValues

# python -m unittest test_utils.py
# python -m unittest discover tests


class TestAdd(unittest.TestCase):
    def test_add(self):
        result = addValues(2, 5)
        self.assertEqual(result, 7)


# if __name__ == "__main__":
#     unittest.main()
