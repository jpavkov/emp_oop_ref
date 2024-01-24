## regular methods = automatically take the instance as the first argument (self)
## class methods = automatically pass the class as the first argument (cls)
## static methods = don't pass anything as argument, but are logically included in class

## creating and instantiating classes
## method: function associated w/ a class
## instance variables: unique to each instance
## class variables: same for all instances

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first  
        self.last = last  
        self.pay = pay
        self.email = first + "." + last + '@company.com'

        Employee.num_of_emps += 1 # Employee is the class level, not self (instance level)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount 

    @classmethod ## alternative constructor
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() in (5, 6):
            return False
        return True


emp_1 = Employee('jon', 'pavkov', 50000)
emp_2 = Employee('bill', 'smith', 65000)

emp_str_1 = 'John-Doe-70000'
emp_3 = Employee.from_string(emp_str_1)

print(emp_1.pay)
print(emp_2.pay)
print(emp_3.pay)

import datetime 
my_date = datetime.date(2024, 1, 24)
print(Employee.is_workday(my_date))
