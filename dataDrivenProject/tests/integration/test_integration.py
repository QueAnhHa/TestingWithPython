"""
Create test_integration.py for integration test
A good technique when testing application with backend database is to store the test data in a folder within integration 
testing folder called fixtures to indicate that it contains test data.
Then within your test case, you can use .setUp() to load the test data from a fixture file in a known path and execute many 
tests against the data.
"""

import unittest



class TestBasic(unittest.TestCase):
	def setUp(self):
		# Load Test Data
		self.app = App(database='fixtures/test_basic.json')


	def test_customer_count(self):
		self.assertEqual(len(self.app.customers), 100)


	def test_existence_of_customer(self):
		customer = self.app.get_customer(id=10)
		self.assertEqual(customer.name, "Org XYZ")
		self.assertEqual(customer.address, "10 Red Road, Reading")



class TestComplexData(unittest.TestCase):
	def setUp(self):
		# load test data
		self.app = App(database='fixtures/test_complex.json')


	def test_customer_count(self):
		self.assertEqual(len(self.app.customers), 10000)


	def test_existence_of_customer(self):
		customer = self.app.get_customer(id=9999)
		self.assertEqual(customer.name, u"banana")
		self.assertEqual(customer.adress, "10 Read Road, Akihabara, Tokyto, Japan")


if __name__ = "__main__":
	unittest.main()

	
