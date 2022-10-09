from random import randint

class Restuarant():

    def __init__(self, resturant_name, cuisine_type):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_resturant(self):
        print(f"Restuarant name:{self.resturant_name}\nCuisine type:{self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.resturant_name} is now open!")

    def set_number_served(self, new_number_served):
        self.number_served = new_number_served

    def increment_number_served(self, increment_number):
        self.number_served = self.number_served + increment_number



rest_1 = Restuarant("Maba", "Indian")
rest_2 = Restuarant("Tiny Shop", "Korean")
rest_3 = Restuarant("Tzuki", "Japanese")

resturants = [rest_1, rest_2, rest_3]

for resturant in resturants:
    resturant.describe_resturant()
    resturant.open_restaurant()
    print("Number served:", resturant.number_served)
    resturant.set_number_served(randint(10,50))
    print("New number served:", resturant.number_served)
    resturant.increment_number_served(randint(25,100))
    print("Number served as of now:", resturant.number_served)

# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote
# in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
# the class will work; just pick the one you like better. Add an attribute called
# flavors that stores a list of ice cream flavors. Write a method that displays
# these flavors. Create an instance of IceCreamStand, and call this method.

# Inheritance

class IceCreamStand(Restuarant):
    """Inherits from the Restaurant class"""

    def __init__(self, resturant_name, cuisine_type):
        # Initialise 
        super().__init__(resturant_name, cuisine_type)
        self.flavours = ["Mango", "Vanilla", "Chocolate", "Pistacchio"]

    def show_flavors(self):
        print("These are the available flavours:", self.flavours)


ics1 = IceCreamStand("K&N CD", "Dessert")
ics1.describe_resturant()
ics1.open_restaurant()
ics1.show_flavors()

# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.

def add_user(first_name, last_name, **kwargs):
    """Add a user to the dictionary of users"""
    user = {}
    user["first_name"] = first_name
    user["last_name"] = last_name
    for key, value in kwargs.items():
        user[key] = value
    users[first_name] = user

    user_del


# def describe_user(user):
    

