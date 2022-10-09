with open("learning_python.txt") as file_object:
    # contents = file_object.read()
    # print(contents.rstrip())
    lines = file_object.readlines()
    new_String = ""
    for line in lines:
        new_String += line.replace("Python", "C").rstrip()
    print(new_String)
