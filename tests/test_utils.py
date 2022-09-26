import unittest
from src.helpers.index import addValues


# from helpers.index import addValues

# python -m unittest test_utils.py


class TestAdd(unittest.TestCase):
    def test_add(self):
        result = addValues(2, 5)
        self.assertEqual(result, 7)


# if __name__ == "__main__":
#     unittest.main()
