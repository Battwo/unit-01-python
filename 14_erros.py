"""
Identify the potential errors in the following code snippets and modify 
them to include appropriate try/except blocks to handle exceptions gracefully.
"""


"""
Example 1: Division
"""
print()
print()
print("--------task 1--------")


def divide_numbers(num1, num2):
    try: #this is annother part of where the code will start to go wrong 
        result = num1 / num2
        print("Result:", result)#you can only divide by numbers that are not zero so this will cause an error 

    except ZeroDivisionError: #the errors name was zero divison error so i have to make note of that. if put the wrong name it will not work
        print("Error: Cannot divide by zero.")#anyime num two is equal to zero this will print out instead of the code talking rubish to me 

# Example usage:
divide_numbers(10, 0)

print()
print()
print("--------task 2--------")
"""
Example 2: Opening Files
"""

def read_file(filename):
    try: #I placed a try here because this is the part where the code will start to fail
        file = open(filename, 'r') #because the fail does not exist this will cause an error
        contents = file.read()
        print("File contents:", contents)
        file.close()
    except FileNotFoundError:
        print("Error: The file was not found.")# this will print out as long as the code continues to fail and give us an error so the we know that its because the file does not exist

# Example usage:
read_file("nonexistent.txt")

print()
print()
print("--------task 3--------")
"""
Example 3: List Items
"""

def get_item(lst, index):
    try:
        item = lst[index]#getting an index that does not exist will cause an error
        print("Item:", item)
    except IndexError:
        print(f"Error: '{index}' is out of range for the list. how about trying a lower number ")#this will happen if user tries to get an index that does not exist in the list but it will also suggest to try a lower number

# Example usage:
my_list = [1, 2, 3]
get_item(my_list, 5)# 5 does not exist in this list so is the reson for why we have an error, if we had used 2 it would have worked fine because 2 is in the list

"""
Example 4: Dictionaries
"""
print()
print()
print("--------task 4--------")


def get_value(dictionary, key):
    try:
        value = dictionary[key]#trying to get a key that does not exist will cause an error
        print("Value:", value)#this is supposed to print the value of the key
    except KeyError:#this will allow the code to run without crashing
        print(f"Error:  '{key}' not found in the dictionary.")
# Example usage:
my_dict = {"a": 1, "b": 2}
get_value(my_dict, "c")

print()
print()
print("--------task 5--------")
"""
Example 5: Else/Finally
Modify the following code to include an else block to execute code if no exceptions occur 
and a finally block to ensure that a certain action is always performed, regardless of whether an exception is raised.
"""
def process_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:", contents)
    except FileNotFoundError:
        print("Error: File not found.")
    finally:
        print("File processed successfully.")#this will print no matter what happens 
# Example usage:
process_file("example.txt")