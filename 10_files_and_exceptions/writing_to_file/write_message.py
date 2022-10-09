import os

filename = "programming.txt"

# Check if file exists else creates a new file.
if os.path.exists(filename):
    print("The file " + filename + " already exists.")
    with open(filename, "a") as file_object:
        file_object.write("I love creating new games.\n")
        file_object.write("I also love finding meaning in large datasets.\n")
        file_object.write("I love creating apps that can run in a browser.\n")
else:
    with open(filename, "w") as file_object:
        file_object.write("I love programming.\n")
