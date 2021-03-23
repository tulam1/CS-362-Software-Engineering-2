#**************************************************************
# *
# * Program: name.py
# * Author: Tu Lam
# * Date: February 4th, 2021
# * Description: The program is to implement a way to display  
# * 				  someone full name as they give two strings input.
# *
#**************************************************************

def f_name(x, y):

	if (x == "" or y == ""):			#If first name is NULL or last name is NULL
		assert(0);
	elif (x == "" and y == ""):		#Else if both first and last name is NULL, return fail
		assert(0);
	else:											#Else if it is perfect, return the full name
		z = x + y;
		return z;
