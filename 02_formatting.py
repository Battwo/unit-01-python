"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive

"""
password ="firefly"

you_type_pass = input("Enter your password")

if you_type_pass.upper() == password.upper():
    print("correct password")
else:
    print("your wrong")

"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""
user_input = "Not empty"
if user_input.strip() =="":
    print("invalid")
else:
    print("valid")



"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""
pet = "Cat"
new_pet = pet.replace ("Cat", "Dog") # I replaced Cat to Dog 

print(new_pet) # I print the new change 



"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""
name = "bob" #added name
age = 19 # added age
print( f"welcome {name} are you sure your {age} years old?") #inputs go here 

"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""

apples = 19/15
oranges = 111/20 

ap = f"result: {apples:.1f}" # added the 2f that changes the decimal place 
Or  = f"result: {oranges:.1f}"

print(ap)
print(Or)
