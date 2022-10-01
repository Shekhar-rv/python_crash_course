class Employee():
    """This class stores an employee's first and last name along with 
    their salary and has a method that gives an employee a pay raise """

    def __init__(self, first_name:str, last_name:str, salary:float) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, amount:float=5000) -> None:
        """Give the employee a raise"""
        self.salary += amount

if __name__ == '__main__':
    employee = Employee(first_name="Sam", last_name="Smith", salary=50000)
    print("Salary before raise:", employee.salary)
    employee.give_raise()
    print("Salary after 1st raise:", employee.salary)
    employee.give_raise(amount=10000)
    print("Salary after 2nd raise:", employee.salary)