# Practice Testing with Python
# Some simple functions to test

def test_sum():
	assert sum([1, 2, 3]) == 6, "should be 6"


def test_sum_tuple():
	assert sum((1, 2, 2)) == 6, "Should be 6"


if __name__ = "__main__":
	test_sum()
	test_sum_tuple
	print("Everything passed")

"""
There are many test runners available in Python. Three most popular test runner are: unittest, nose or nose2 and pytest.
unittest requires that:
	You put your tests into classes as methods
	You use a series of special assertion methods in the unittest.TestCase class instead of the built-in assert statement """

# Rewrite the test for those functions above with unittest
import unittest


class TestSum(unittest.TestCase): # inherit from TestCase class


	def test_sum(self):
		self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")


	def test_sun_tuple(self):
		self.assertEqual(sum(1, 2, 2), 6, "Should be 6")


if __name__ = "__main__":
	unittest.main()

# Using nose2 from PyPi 
pip install nose2
python -m nose2

# nose2 will try to discover all test scripts named test*.py and test cases inheriting from unittest
# pytest suopports execution of unittest test cases. We can use the script at the top to run with pytest
