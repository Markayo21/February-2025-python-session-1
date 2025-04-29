#input()= a function that prompts the user to enter data 
#         Returns the entered data as a string


name = input("What is your name?:")

#If you want to perform an arithmetic function you convert your string to integer
age = int(input("How old are you?:"))

# 0r use this input  age = int(age)
age = age + 3

print(f"Hello {name}!")
print(f"You are {age} years old!")
