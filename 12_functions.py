"""
Task 1: Greeting
Write a function that takes a name as a 
agrument and prints a greeting message like "Hello, [name]!".
"""
print()
print()
print("--------task 1--------")

def my_funnyfunction(name): #i created a funnction that would print the hello along with the persons name. 
    print("Hello " + name)

my_funnyfunction("Alice")

"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
print()
print()
print("--------task 2--------")

def Square_num(a):
    return a ** 2 #this will Square the number 

x = Square_num(8) #we made a = to 8 so the result should print to 8^2 which is 64 
print(x)
"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns `True` if the number is even, and `False` otherwise.
"""
print()
print()
print("--------task 3--------")

def true_false(x):
    return x % 2 == 0 # this is what determs that the number is ether even or odd
print(true_false(4)) #if 4 is even it will print true 
print(true_false(11)) 




"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""
print()
print()
print("--------task 4--------")

def Rectangle(l,w): #the length and width of the rectangle 
    return l * w #multiplys the two numbers 
area = Rectangle(5,7) # this will 
print(area)

"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
print()
print()
print("--------task 5--------")

def temperature(Celsius):
    return Celsius * 4 + 50 #the formula to turn Celsius to Fahrenheit
print(temperature(10)) #this would be the "Celsius" which is 10 and in fahrenheit it would be 90 

"""
Task 6: Average of Numbers
Write a function that takes a list of numbers as an argument
and returns the average (mean) of those numbers.
"""
print()
print()
print("--------task 6--------")

def list_numbers(number):
    return sum(number) / len (number) # this will add up all numbers and divide them by the amont of numbers in the list 
print(list_numbers([1,2,3,4,5,6,7,8,9,10])) # i made the list 



"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, 
and returns the total.

Your function should also optionally accept a 3rd argument for discount as a float, 
and return the discounted if provided.
"""
print()
print()
print("--------task 7--------")

def Calculator (price,quantity,discounted = 0.0 ):
    total = price * quantity

    if discounted >0:
        total = total - (total * discounted)
    return total

print("Total without discount:", Calculator(50, 3))  