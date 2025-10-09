"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
print()
print()
print("----task 1 ----" )
print()
print()
for i in range(1, 11): #It starts at 1 and It ends at 10.
    print(i) # this will print 



"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
print()
print()
print("----task 2 ----" )
print()
print()
for i in range(900, 1001, 10): #Start at 900, it add 10 each time and stop at 1000

    print(i) #this will pint it


"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""
print()
print()
print("----task 3 ----" )
print()
print()
for i in range(1, 101, 9): # Start at 1, add 9 every time and stops when it goes over 100

    print(i) #This will print


"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""
print()
print()
print("----task 4 ----" )
print()
print()

total = 0 # Start with 0 
for i in range(1, 11): #Add 1 up to 10 
    total += i 

print("Sum:", total) #how the total at the end 


"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

- Explain the iterative process that this code executes to get that output
"""
print()
print()
print("----task 5 ----" )
print()
print()
rows = 5 # made row equal to 5 
for i in range(rows):#create for loop for rows
     for j in range(i + 1):#create for loop for columns
         print('*', end=' ')#print star and end with a space
     print() #it prints 