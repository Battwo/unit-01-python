# Import necessary modules
import  os  # Provides functions to interact with the operating system
import sys   # Provides access to variables and functions that interact with the Python interpreter


"""
Task 1 (os module): 
Write a Python program that prints the current folder (working directory) using the os module.
"""
print("--task 1--")
print()
print()
print("Current directory is:", os.getcwd()) # Get and print the current working directory
print()



"""
Task 2 (os module):
Create a new directory called "test_folder" in the current directory.
Then print a list of all files and directories in the current directory.
"""
print("--Task 2--")
print()
print()





# Create a folder named 'test_folder' if it doesn't already exist
os.makedirs("test_folder", exist_ok=True)

# List and print everything in the current folder
print("Items in this folder:")
for item in os.listdir():  # Loop through all items in the current directory
    print("-", item)       # Print each item (file or folder)
print()






"""
Task 3 (os module):
Write a program that checks if a directory called "data" exists in the current
working directory. If it doesn't exist, create it. If it does exist, print
"Directory already exists."
"""
print("--Task 3--")
print()
print()




# If the 'data' folder exists, say so
if os.path.isdir("data"):
    print("'data' folder already exists.")
else:
    # If it doesn't exist, create it
    os.mkdir("data")
    print("'data' folder was created.")
print()




"""
Task 4 (os.path module):
Write a program that checks if a file called "config.txt" exists in the current directory.
If it exists, print its path. If it doesn't exist, print "File not found."
"""
print("--task 4--")
print()
print()




# this will define the filename
file_name = "config.txt"


# this check if the file exists
if os.path.isfile(file_name):
   # this will get the absolute path
   file_path = os.path.abspath(file_name)
   print("File found at:", file_path)
else:
   print("File not found.")



"""
Task 5 (sys module):
Write a program that prints the Python version you are currently using.
"""
print("------Task 5-------")
print()
print()
print("Python Version:")
print(sys.version)


print("\nVersion Info (tuple format):")
print(sys.version_info)



"""
Task 6 (sys module):
Write a program that prints the platform your Python interpreter is running on
(e.g., 'linux', 'win32', 'darwin'). The output should be user friendly names
"Linux", "Windows", "MacOS"
"""
print("---task 6--")
print()
print()




# Get the platform string
platform = sys.platform


# Map the platform string to user-friendly names
if platform.startswith('linux'):
   friendly_name = 'Linux'
elif platform == 'win32':
   friendly_name = 'Windows'
elif platform == 'darwin':
   friendly_name = 'MacOS'
else:
   friendly_name = f'Unknown platform: {platform}'


# Print the result
print(f"You are running on: {friendly_name}")

