from name_function import get_formatted_name

print("Enter 'q' to quit the input!")

while True:
    first_name = input("Please enter your first name: ")
    if first_name == 'q':
        break
    last_name = input("Please enter your last name: ")
    if last_name == 'q':
        break

    full_name = get_formatted_name(first=first_name, last=last_name)
    print(f"Neatly formated full name: {full_name}")