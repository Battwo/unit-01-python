"""
Task 1 (random module):
Write a program that simulates rolling a six-sided die 10 times.
Print each roll result.
"""
# Import necessary module
import random

print()
print()
print("--------task 1--------")
attempts = 0 # I made attemps equal zero so that you can start
max_attempts = 10 # max attemps is here in order to stop the user from rolling more then 10 times 

while True: 
    print("roll your dice")
    result = random.randint(1, 6)
    attempts += 1
    print (result)
    print("___________")
   

    if attempts >= max_attempts:
        print("Too many attempts")
        break
    


"""
Task 2 (random module):
Write a program that generates 5 random floating-point numbers between 0 and 1.
Then generate 5 random floating-point numbers between 10 and 20.
Print both sets of numbers.
"""

print()
print()
print("--------task 2--------")

for _ in range(5): #will only go 5 times 
    print(random.random()) # prints 
    print("-------0-1----------")

randoms = [random.uniform(10, 20) for _ in range(5)] # this will picl a number from 10 to 20  5 times randomly 
print(randoms) #prints 
print("--------10-20-------")


    
 


"""
Task 3 (random module):
Create a list of colors: ["red", "blue", "green", "yellow", "purple"].
Write a program that randomly selects and prints 3 colors from this list without replacement.
"""

print()
print()
print("--------task 3--------")
#I made a list called my_list 
my_list = ["red", "blue", "green", "yellow", "purple"] #this is the things in my list 
print(random.choice(my_list)) #this will print a random color from the list 


"""
Task 4 (random module):
Write a program that creates a list of numbers from 1 to 10, then shuffles the list
and prints the shuffled result.
"""
print()
print()
print("--------task 4--------")

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #I made a  list from 1-10 
#shuffle the list
random.shuffle(my_list)
print(my_list)