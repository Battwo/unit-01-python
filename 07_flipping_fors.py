"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""
print()
print()
print("------task 1------")
print()
print()

fire_dogs = "My dog" 

for x in fire_dogs:
    print(x) # do i really have  to explane? , i just printed each character 



"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""
print()
print()
print("------task 2------")
print()
print()
num = [5, 10, 15, 20] # made a list with numbers
sum = 0
for x in num:
 sum += x #I added the sum
 print(sum)





"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""
print()
print()
print("------task 3------")
print()
print()
p = "i love dogs" # I made a sentince 
words = p.split(" ") # I turned my sentince into a list and saved it 

for x in words:
   print (len(x)) # gor the lenught!






"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result

In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""

print()
print()
print("------task 4------")
print()
print()
my_dict = { #I made a Dictionary

   "dogs": 8, # added my keys and valus 
   "cats": 20,
   "bird": 1
}

for x in my_dict:
   print(x) 
   #I noticed that the only thing that printed was the KEYS, I only saw that dogs, cats, and bird printed but the VALUS like 8, 20, and 1 did not print
   #honeslty I expected that the keys and valus would be printed side by side 