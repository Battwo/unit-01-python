print("Hello")

"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""
#added a variable
Alexannys_float = 12.2
#converted my float into an integer
my_integer= int(Alexannys_float)
#I printed both variables
print(Alexannys_float)
print(my_integer)




"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""
age = 10
#I made a variable
if age < 0:
    print("negative") #I made it print if age is less then 0
elif age > 0:
    print("positive") #age will print positive if more then
else:
    print("zero") #if zero it will print zero 




"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""
print()
print()
print()


input1 = input("give me a float :") # added an input 
num1 = float(input1)

print(type(num1))

"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""
my_dict = {
     'oranges': 89, #I added the key oranges and gave it the value 89
    'bananas': 3, #I added the key bananas and gave it the value 3
    'apples': 10 #I added the key apples and gave it the value 10
    }


print('oranges')
print('bananas')
print('apples')

"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""

"""
TASK 6:

Create a list of your favorite subjects (as strings). 
Use the join() function to combine all subjects into a single string separated by commas.
Then create another version using " - " as the separator.
Print both the original list and both joined strings.
"""