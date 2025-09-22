
"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
apple = 1 # set apple to one

while apple < 10: # while apple is less them 10 the loop will keep going 
    print(apple)
    apple += 1 # will slowly added apple up by 1 until it reaches ten




"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""

m = 10 # set m to 10

while m > 0:  #while m is more then zero problem will keep going 
    print(m)
    m -= 1 # will slowly subtract m by 1 until it reaches zero


"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
number = int(input("give a number:  ")) #user will put a number in here 
result = 1

while number > 0: # while the number is more then zero prolem will work. if its equal to zero it wont work, you cant mulitlply by zero
    print(number) 
    print()
    result = number * result #so because the data is being saved  the "number" would keep decressing the "result" would keeo incressing and then both numbers will mulityply at the end 
    number -= 1

print(result)

"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
passworld = "1981"
user_input = ""

while user_input != passworld: # if the user_input is not password it will do the next step 
     user_input = input("password is romeo santos birth year") # will give you a hint of the password
     if user_input == passworld: #if password correct it will print good job and stop the loop
         print("good job! You got it!!!")
     else:  
         print( " try once more") # if you got password wrong it will keep asking you to try once more 

"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""


"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""

