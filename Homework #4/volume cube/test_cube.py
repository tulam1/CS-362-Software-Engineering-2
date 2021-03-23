#**************************************************************
# *
# * Program: test_cube.py
# * Author: Tu Lam
# * Date: February 4th, 2021
# * Description: The program is to hold test case for the volume 
# * 				  calculation.
# *
#**************************************************************

import unittest
import cube

class TestCase(unittest.TestCase):
	def test1(self):
		self.assertEqual(cube.volume_cube(2), 8)

	def test2(self):
		self.assertEqual(cube.volume_cube(-1), 0)

	def test3(self):
		self.assertEqual(cube.volume_cube(2.3), 12.167)

if __name__ == '__main__':
	unittest.main(verbosity=2)
