def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = " ".join([first, last])
    return full_name.title()


if __name__ == "__main__":
    test_name = get_formatted_name("pickle", "tickle")
    print(test_name)