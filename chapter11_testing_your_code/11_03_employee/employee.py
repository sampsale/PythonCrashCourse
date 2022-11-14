

class Employee:
    def __init__(self, first_n, last_n, salary):
        self.first_name = first_n
        self.last_name = last_n
        self.salary = salary
    def give_raise(self, salary= 5000):
        self.salary += salary