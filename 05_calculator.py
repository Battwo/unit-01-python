import math 

print("Welcome to my Calculatinator") # this will welcome you to the page
print()
print()
print()

Number1 = int( input("Enter the first number")) # user inputs the first number here

Number2 = int( input("Enter the second number")) # user imputs the secound number here

print()
print()
print()
print()

print("Select operation") # I gave the options of the Operations the user can pick from
print()
print()
print()
print("1. Addition") 
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Floor Division")
print("6. Exponential")
print("7. Remainder")

choice = int( input("Enter your choice"))
             
if choice == 1:
    result = Number1 + Number2 # I made whatever number 1 is to be added to whatever number 2 is
    print(result)
if choice == 2:
    result = Number1 - Number2  # I made whatever number 1 is to be subtracted from whatever number 2 is
    print(result)
if choice == 3:
    result= Number1 * Number2 # I did multipliction if chpice is 3
    if Number1 == 0:
        print("you cant use zero") #stops you from Multiplying with 0
    if Number2 == 0:
        print("can not be zero")
    print(result)
if choice == 4:
    result= Number1 / Number2 #if choice is equal to 4 which is Division it will divided both numbers
    print(result)
if choice == 5:
    result= Number1 // Number2 #if choice is equal to 5 which is floor Division it will do floor divison
    print(result)
if choice == 6:
    result = Number1 ** Number2 # if its choice exploential which is 6 then the two numbers will work based off that 
    print(result)
if choice == 7: 
    if Number2 == 0:
        print ("invalid") 
    else:
        result = Number1 % Number2 # will give you the remainder if choice is 7 
        print(result)
if choice <1 or choice < 7:
    print("invalid operation") #there are no other options so if any option is not as the ones listed it will be invaled
 


