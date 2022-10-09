def get_formatted_name(first, last, middle=""):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = " ".join([first, middle, last])
    else:
        full_name = " ".join([first, last])
    return full_name.title()


if __name__ == "__main__":
    test_name = get_formatted_name("pickle", "tickle")
    print(test_name)
