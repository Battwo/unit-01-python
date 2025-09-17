"""Task 1: Create a list
Create a list with 4 elements and print it.
"""

Elements0 = ["water", "fire", "metel", "air"] #list of elements
print( Elements0)


"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""
elements = ["water", "fire", "metel", "air"]
elements.append ("wood") # added an element

print(elements) #printed a new element
"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""
Elements1 = ["water", "fire", "metel", "air","wood"] #list of elements
Elements1.remove("wood") #removing wood
print(Elements1)
"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""
Elements2 = ["water", "fire", "metel", "air","wood"] #list of elements
Elements2[1] = "light" # changing fire to light
print(Elements2)
"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""

Elements3 = []
Elements3.append ( "fire" ) #adding fire to list
print(Elements3)
Elements3.append ( "water" ) #adding water
Elements3.append ( "air" ) # I added air 

print( Elements3)



"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""
Elements4 = ["Hydrogen", "Helium","Lithium"] #I have a list

Elements4.remove("Lithium") #I removed Lithium

print (Elements4) #printed element4

Elements4 = ["Hydrogen", "Helium"] #new list

Elements4.remove("Helium") #removed Helium

print (Elements4)


"""
Task 7: Slicing lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""
elements5 = ["Beryllium","Boron", "Carbon"] #made another list

no_fire = elements5[2] #honestly I sent it equal to element 2 

print(no_fire)




"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""

names_1 = ["bob", "jake", "emma"] # made a list of names

names_2 = ["kate", "lukcy", "alex"] #made another

names = names_1 + names_2 # I extended it

print(names)