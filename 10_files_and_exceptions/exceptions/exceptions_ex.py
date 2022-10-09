# Addition: One common problem when prompting for numerical input
# occurs when people provide text instead of numbers. When you try to convert
# the input to an int, you’ll get a TypeError. Write a program that prompts for
# two numbers. Add them together and print the result. Catch the TypeError if
# either input value is not a number, and print a friendly error message. Test your
# program by entering two numbers and then by entering some text instead of a
# number.

# Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
# so the user can continue entering numbers even if they make a mistake and
# enter text instead of a number.


def addition():
    while True:
        try:
            number_1 = float(input("Enter the first number to add: "))
            number_2 = float(input("Enter the second number to add: "))
        except ValueError:
            print("Please enter a numerical input")
        else:
            print(number_1 + number_2)
            break


# Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three
# names of cats in the first file and three names of dogs in the second file. Write
# a program that tries to read these files and print the contents of the file to the
# screen. Wrap your code in a try-except block to catch the FileNotFound error,
# and print a friendly message if a file is missing. Move one of the files to a dif-
# ferent location on your system, and make sure the code in the except block
# executes properly.

# Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
# silently if either file is missing.


def content_viewer(file_name):
    try:
        with open(file_name) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        # print(f"The {filename} could not be found, please check the file name.")
        pass  # To fail silently.
    else:
        print(contents)


# Common Words: Visit Project Gutenberg (http://gutenberg.org/ )
# and find a few texts you’d like to analyze. Download the text files for these
# works, or copy the raw text from your browser into a text file on your
# computer.You can use the count() method to find out how many times a word or
# phrase appears in a string. For example, the following code counts the number
# of times 'row' appears in a string. Converting the string to lowercase using
# lower() catchesall appearances of the word you’re looking for, regardless of how it’s
# formatted. Write a program that reads the files you found at Project Gutenberg and
# determines how many times the word 'the' appears in each text.


def word_counter(file_name):
    try:
        with open(file_name) as file_object:
            content = file_object.read()
            word_count = content.lower().count("the")
    except FileNotFoundError:
        print(f"The {filename} could not be found, please check the file name.")
        # pass # To fail silently.
    else:
        print(
            f"In the file {file_name} the are {word_count} instances of the word 'the'."
        )


if __name__ == "__main__":
    # addition()
    # filenames = ['cats.txt', 'dogs.txt', 'ferrets.txt']
    # for filename in filenames:
    #     content_viewer(filename)
    filenames = ["alice.txt", "blindfold.txt", "anthem.txt", "test.txt"]
    for filename in filenames:
        word_counter(filename)
