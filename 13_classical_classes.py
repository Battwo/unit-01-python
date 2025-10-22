"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
print()
print()
print("--------task 1--------")

class Person: #i created a class called person
    species = 'Homosapien'#this is the attribute

    def __init__(self,name, age): #I added attributes like name and age 
        self.name = name
        self.age = age 
        age = str(self.age) #converting age to a string so it can be printed
    

    def intro(self): #made a method for intoduction
        print("Hello my name is " + self.name + " and I am " + str(self.age) + " years old." )

name = Person("lilly", 28) 
name.intro()


"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""
print()
print()
print("--------task 2--------")
class Animal: #base class
    def speak(self):# i made an empty method
        pass # I made a pass so it does nothing
class Dog(Animal): #this  is the dog class
    def speak(self):
        return "Woof"#will make a dog sound 
class cat(Animal): #this is the cat class
    def speak(self):
        return "meow" #makes a cat sound 
doggo = Dog() #created an instance of dog
catto = cat() #created an instance of cat
print("dog makes the sound " + doggo.speak()) #will print the sound for the dog langage
print("cat make makes the sound " + catto.speak()) #will print the sound for the cat langage
    
    



"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""