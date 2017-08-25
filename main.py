#   main.py
#   CompareThreeNumbers_Python
#
#   This program will help you get the size of a phrase given by the user, and let you
#   know if that size is an even or odd number.
#
#   Python interpreter: 3.6
#
#   Author: León Felipe Guevara Chávez
#   email:  leon.guevara@itesm.mx
#   date:   May 29, 2017
#

#   We ask for and read three numbers
number1 = float(input("Give me the first number: "))
number2 = float(input("Give me the second number: "))
number3 = float(input("Give me the third number: "))

#   We find which of the three numbers is the biggest
if number1 >= number2 and number1 >= number3:
    biggest = number1
elif number2 >= number1 and number2 >= number3:
    biggest = number2
else:
    biggest = number3

#   We display our findings
print("The biggest number among the three is: " + str(biggest))
