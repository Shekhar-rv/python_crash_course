# Guest: Write a program that prompts the user for their name. When they
# respond, write their name to a file called guest.txt.
def guest(filename="guest.txt"):
    with open(filename, "w") as file_object:
        name = input("What is your name? ")
        file_object.write(name)


# Guest Book: Write a while loop that prompts users for their name. When
# they enter their name, print a greeting to the screen and add a line recording
# their visit in a file called guest_book.txt. Make sure each entry appears on a
# new line in the file.


def guest_book(filename="guest_book.txt"):
    while True:
        name = input("What is your name? ")
        if name == "q":
            break
        else:
            with open(filename, "a") as file_object:
                file_object.write(name + "\n")


# Programming Poll: Write a while loop that asks people why they like
# programming. Each time someone enters a reason, add their reason to a file
# that stores all the responses.


def programming_poll(filename="programming_poll.txt"):
    while True:
        reason = input("Why do you like programming? ")
        if reason == "q":
            break
        else:
            with open(filename, "a") as file_object:
                file_object.write(reason + "\n")


if __name__ == "__main__":
    # guest()
    # guest_book()
    programming_poll()
