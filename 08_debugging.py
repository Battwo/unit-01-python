text = "Hello, world, my name is" #Count how many spaces are in a given string


count = 0

for char in text:
    if char == " ":# PROLEM ON THIS LINE
       count += 1

print(count)





print("give me a number") #Determine if numbers 1 to n are even or odd 


n = int(input())#MAYBE HERE TOO 

for num in range(1, n):
    if num % 2 == 0: #THE ISSUE WAS HERE
        print(num, "is even.")
    else:
        print(num, "is odd.")






attempts = 0
correct_password = "secret"

while True:
    password = input("Enter your password: ")
    attempts += 1

    if password == correct_password
        print("you got the password correct")
        break


    if password == "incorrect_password":
        print("Correct password!")
    else:
        print("Incorrect password")

    if attempts > 3:
        print("Too many attempts")
        break





