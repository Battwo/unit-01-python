"""
Task 1 (random module):
Write a program that simulates rolling a six-sided die 10 times.
Print each roll result.
"""
from random import randint


attempts = 0 # I made attemps equal zero so that you can start
max_attempts = 10 # max attemps is here in order to stop the user from rolling more then 10 times 

while True: 
    print("roll your dice")
    reslut = randint(1, 6)
    attempts += 1
    print (reslut)
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



"""
Task 3 (random module):
Create a list of colors: ["red", "blue", "green", "yellow", "purple"].
Write a program that randomly selects and prints 3 colors from this list without replacement.
"""


"""
Task 4 (random module):
Write a program that creates a list of numbers from 1 to 10, then shuffles the list
and prints the shuffled result.
"""