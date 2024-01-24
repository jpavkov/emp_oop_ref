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

emp_1 = Employee('jon', 'pavkov', 50000)
emp_2 = Employee('bill', 'smith', 65000)

emp_1.raise_amount = 1.06
emp_1.apply_raise()
print(emp_1.pay)
print(emp_1.__dict__)

print(Employee.num_of_emps)
