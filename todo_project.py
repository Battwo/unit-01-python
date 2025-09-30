print()
print("welcome To your to do list!")

print()
your_list = []


while True:
  
    for x in your_list:
        print(x) 

    print("\n" + "~" * 50 + "\n")

    question = input("would you like to add, remove a todo or clear?").strip()
    if question == "add":
       items = input("what would you like to add to your list")
       your_list.append(items)
    
   

    if question == "remove":
        remove_items = input("what would you like to remove from your list")
        your_list.remove(remove_items)
    
    print("\n" + "~" * 50 + "\n")

    if question == "clear":
        your_list.clear()

 
 


