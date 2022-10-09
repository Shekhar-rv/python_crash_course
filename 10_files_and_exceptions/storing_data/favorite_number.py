from json import dump, load


def retrieve_stored_num() -> float:
    """Show the favorite number stored"""
    filename = "favorite_num.json"
    try:
        with open(filename) as f_obj:
            favorite_number = load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return favorite_number


def request_favorite_number() -> None:
    """Requests and stores user's favorite number"""
    fav_num = float(input("Please enter your favorite number: "))
    filename = "favorite_num.json"
    with open(filename, "w") as f_obj:
        favorite_number = dump(fav_num, f_obj)


def run() -> None:
    user_favorite_number = retrieve_stored_num()
    if user_favorite_number:
        print(f"I know your favorite number! It's {user_favorite_number}")
    else:
        user_favorite_number = request_favorite_number()
        print("Your favorite number is saved!")


if __name__ == "__main__":
    run()
