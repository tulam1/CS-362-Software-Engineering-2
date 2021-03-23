#**************************************************************
# *
# * Program: test_name.py
# * Author: Tu Lam
# * Date: February 4th, 2021
# * Description: The program is to hold test case for the full 
# * 				  name.
# *
#**************************************************************

import unittest
import name

class TestCase(unittest.TestCase):
	def test1(self):
		self.assertEqual(name.f_name("John ", "Smith"), "John Smith")

	def test2(self):
		self.assertEqual(name.f_name("", ""), "")

	def test3(self):
		self.assertEqual(name.f_name("Kylie ", ""), "Kylie ")

if __name__ == '__main__':
	unittest.main(verbosity=2)
