#File Handling and Error Handling

#Opening a file in read mode
file = open("example.txt", "r")

""" The first argument to open() is the file path, and the second argument is the mode:

"r": Read mode (default)
"w": Write mode (creates a new file or overwrites an existing file)
"a": Append mode (adds content to the end of the file)
"b": Binary mode (used for non-text files like images) """

""" with open("example.txt", "r") as file:
    content = file.read()
    print(content)
 """
#writing to files
""" with open("output.txt", "w") as file:
    file.write("Hello, world!")
    file.write("Second message")
 """
""" When you open a file in write mode ("w"), the file is overwritten if it already exists.  """

#working with large File
""" with open("large_file.txt", "r") as file:
    for line in file:
        print(line.strip()) """

#Working with file paths using the os Module
#Getting the current working directory
import os
#print(os.getcwd()) #cwd=currentworkingdirectory

#creating, renaming and deleting files or directories
#creating directory
#os.mkdir("new_folder")#mkdir = make directory

#Rename a file or directory
""" os.rename("large_file.txt", "new_name.txt") """

#Remove a file: Use os.remove() to delete a file.
#os.remove("example.txt")

#Check if a file exists: 
""" if os.path.exists("output.txt"):
    print("File exists") """

#Joining and Splitting paths
""" file_path = os.path.join("folder", "subfolder", "file.txt")
print(file_path)  """ # Output: folder/subfolder/file.txt (on Unix systems)

#Exception Handling
#Basic Exception Handling
""" try:
    file = open("Out_date.txt", "r")
except FileNotFoundError:
    print("File not found!") """

#Multiple Exception Types
""" try:
    result = 10/0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}") """

#The finally Block
""" try:
    file = open("example.txt", "r")
finally:
    file.close() #EThis runs even if an error occurs """

#word count program
""" def word_count(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            word_count = sum(len(line.split()) for line in lines)
            char_count = sum(len(line) for line in lines)
            print(f"Lines: {len(lines)}")
            print(f"Words: {word_count}")
            print(f"Characters; {char_count}")


    except FileNotFoundError:
        print("File not found!")

word_count("new_name.txt") """

#log Analysis
def analyze_log(file_path):
    try:
        with open(file_path, "r") as file:
            for line in file:
                if "ERROR" in line:
                    print(line.strip())
    except FileNotFoundError:
        print("Log file not found!")

analyze_log("output.txt")