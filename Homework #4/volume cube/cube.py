#**************************************************************
# *
# * Program: cube.py
# * Author: Tu Lam
# * Date: February 4th, 2021
# * Description: The program is to implement a way to calculate 
# * 				  the volume of a cube by asking user dimension
# *				  of the cube they want to calculate.
# *
#**************************************************************

# This function help to calculate the volume of a cube
def volume_cube(x):
	result = int(0);				# Declare an int named result
	result = x * x * x;			# Multiply the input 3 times to get the volume
	return result;					# Return the result of the volume


input_s = 0;							# Assign a variable for input and sotre variable to use in function
y = 0;

while True:
	input_s = input("Enter a number to calculate the volume of the cube in that dimension: ");
	
	if (isinstance(input_s, int)):# If the number enter is a whole number, break from the loop
		y = int(input_s);				# Make a number
		if (y > 0):						# If the number bigger than 0, break
			break;
		else:								
			print("The number you enter is either negative or zero. Please enter a positive number\n");
	else:
		print("The number you enter is either a string or a floating number. Please try again.\n");

vol = volume_cube(y);				# Calculate the result
print("\n");
print("The result and the volume is:", vol);
