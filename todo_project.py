print()
print("welcome To your to do list!")

with open("todo.txt") as file: 

    contents = file.readlines()

print(contents)

print()
your_list = [] # I made an empty list so that I could add more to it 


while True:
  
    for x in your_list: # this will print the list once the loop starts from the top agine 
        print(x) 



    print("\n" + "~" * 50 + "\n") #this will make space, it's there for aesthetic also to keep everything clear

    question = input("would you like to add, remove, clear or exit todo?").strip().lower() # this question is ment for the user to pick an option
    if question == "add":
       items = input("what would you like to add to your list") #when user types add they have the option to add anything to their list and it wass be added 
       your_list.append(items)
    
   

    if question == "remove": #when user clicks remvoe they can take away things from you list 
        print()
        remove_items = int(input("what would you like to remove from your list, Pick according to the number in which your list is displayed")).strip().lower()
        del your_list[remove_items-1]
    
    print("\n" + "~" * 50 + "\n")

    if question == "clear":
        your_list.clear()
        print("you have nothing in your list.") # this lets you get rid of everything in your list 

    if question == "exit":
        file.writelines(your_list)
        break

 
 


