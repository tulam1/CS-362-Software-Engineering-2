#**************************************************************
# *
# * Program: test_element.py
# * Author: Tu Lam
# * Date: February 4th, 2021
# * Description: The program is to hold test case for the average 
# * 				  element in a list.
# *
#**************************************************************

import unittest
import element

class TestCase(unittest.TestCase):
	def test1(self):
		self.assertEqual(element.avg_ele([5,4,6]), 5)

	def test2(self):
		self.assertEqual(element.avg_ele([]), 0)

	def test3(self):
		self.assertEqual(element.avg_ele([0,0]), 0)

if __name__ == '__main__':
	unittest.main(verbosity=2)
