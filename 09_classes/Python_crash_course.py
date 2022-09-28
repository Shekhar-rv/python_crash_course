from random import randint

class Restuarant():
    """ """
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

# Creating class instances 
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


class User():
    """ """
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}, who comes from {self.city} is {self.age} years old!")

    def greet_user(self):
        print(f"Hello {self.first_name}, welcome back to the Matrix!")

    def increment_login_attempts(self, increment_number=1):
        self.login_attempts += increment_number

    def reset_login_attempts(self):
        self.login_attempts = 0

# Create a few class instances

user1 = User("Agent", "Smith", 43, "Zion")
user2 = User("Morpheus", "Kingmaker", 46, "Zion")
user3 = User("Thomas", "Anderson", 32, "Downtown, Capital")
user4 = User("Trinity", "Hacker", 29, "Zion")

users = [user1, user2, user3, user4]

for user in users:
    user.describe_user()
    user.greet_user()
    print("login_attempts:", user.login_attempts)
    user.increment_login_attempts(randint(10, 20))
    print("updated_login_attempts:", user.login_attempts)
    user.reset_login_attempts()
    print("Login attempts have been cleared")
    print("new_login_attempts:", user.login_attempts)


# 9-7. Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
# or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
# of strings like "can add post", "can delete post" , "can ban user" , and so on.
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin, and call your method.

# 9-8. Privileges: Write a separate Privileges class. The class should have one
# attribute, privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges instance
# as an attribute in the Admin class. Create a new instance of Admin and use your
# method to show its privileges.

class Admin(User):
    """ """
    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = Privileges().show_privileges()


class Privileges():
    """ """
    def __init__(self):
        self.privileges = ["can add post", "can delete post" , "can create new user", "can ban user"]

    def show_privileges(self):
        return self.privileges


admin1 = Admin("Admin", "", 0, "The Web")

admin1.describe_user()
admin1.greet_user()
print(f"These are the privileges of the Admin: {admin1.privileges}")

# 9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
# Add a method to the Battery class called upgrade_battery(). This method
# should check the battery size and set the capacity to 85 if it isn’t already.
# Make an electric car with a default battery size, call get_range() once, and
# then call get_range() a second time after upgrading the battery. You should
# see an increase in the car’s range.

class Car():
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")


class Battery():
    """A simple attempt to model a battery for an electric car.""" 

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.") 

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """ Changes the battery size to 85 if its 70."""
        if self.battery_size == 70:
            self.battery_size = 85


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()