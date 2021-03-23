#**************************************************************
# *
# * Program: element.py
# * Author: Tu Lam
# * Date: February 4th, 2021
# * Description: The program is to implement a way to calculate 
# * 				  the average element in a list.
# *
#**************************************************************

def avg_ele(lst):
	if (len(lst) == 0):					# If list is empty 
		assert(0);
	elif (sum(lst) / len(lst) == 0):
		assert(0);
	else:										# Else return the average of the element in list
		return sum(lst)/len(lst);
