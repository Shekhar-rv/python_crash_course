from json import load, dump

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as file_object:
        dump(username, file_object)
    return username

def greet_user():
    '''Load the username, if it has been stored previously.
     Otherwise, prompt for the username and store it.'''
    username = get_stored_username()
    current_user = input(f"Is this your username: {username}, 'yes' or 'no'? ")
    if current_user == 'no':
        username = get_new_username()
    else:
        if username:
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"Next time you login, we will remember you, {username}")

if __name__ == '__main__':
    greet_user()