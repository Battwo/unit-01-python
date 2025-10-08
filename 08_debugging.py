text = "Hello, world, my name is" #Count how many spaces are in a given string


count = 0

for char in text:
    if char == " ":# PROLEM ON THIS LINE
       count += 1

print(count)





print("give me a number") #Determine if numbers 1 to n are even or odd 


n = int(input())#MAYBE HERE TOO 

for num in range(1, n):
    if num % 2 == 0: #THE ISSUE WAS HERE2
        print(num, "is even.")
    else:
        print(num, "is odd.")





num = int(input("Enter an integer: ")) #I fixed the range to include the number, used commas for printing, and changed the condition to reject all negative numbers. 

if num < 0:
    print("No negative numbers.")
else:
    result = 1
    for i in range(1, num + 1):
        result *= i

    print("Factorial of", num, "is", result)




attempts = 0
correct_password = "secret"
max_attempts = 3

while True:
    password = input("Enter your password: ")
    attempts += 1

    if password == correct_password:
        print("Correct password!")
        break
    else:
        print("Incorrect password")

    if attempts >= max_attempts:
        print("Too many attempts")
        break
