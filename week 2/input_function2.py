#exercise 1Write a Python program that asks the user to input two numbers.
Number_1 = int(input("Enter number:"))
Number_2 = int(input("Enter number:"))

#Perform the following operations:

#Addition
Addition = Number_1 + Number_2

#Subtraction
Subtraction = Number_1 - Number_2

#Multiplication
Multiplication = Number_1 * Number_2

#Division (ensure you handle division by zero errors)

try:
   Division = Number_1 / Number_2

except ZeroDivisionError:
  Division= "Error:  Division by zero is not allowed."

#or use the if-else function
#   
#if Number_2 == 0:
#    print("Error: Division by zero is not allowed.")
#else:
#    result = number_1 / number_2
#    print(f"The dividend is {Division})

#Display the results to the user20
print(f"The sum is {Addition}")
print(f"The difference is {Subtraction}")
print(f"The product is {Multiplication}")
print(f"The dividend is {Division}")









