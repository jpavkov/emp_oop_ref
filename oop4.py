## class inheritance with subclasses

class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first  
        self.last = last  
        self.pay = pay
        self.email = first + "." + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    raise_amount = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) # passes this to employee init method to let that class handle init
        self.prog_lang = prog_lang 

class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay) # passes this to employee init method to let that class handle init
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())
   




dev_1 = Developer('jon', 'pavkov', 50000, 'python')
dev_2 = Developer('bill', 'smith', 75000, 'python')
dev_3 = Developer('tommy', 'boy', 110000, 'python')

man_1 = Manager('jeremy', 'todd', 65000)
man_1.add_emp(dev_1)
man_1.add_emp(dev_2)
man_1.add_emp(dev_3)

man_1.print_emps()
man_1.remove_emp(dev_2)
man_1.print_emps()

print(isinstance(man_1, Manager))
print(isinstance(man_1, Developer))
print(isinstance(man_1, Employee))
print(issubclass(Manager, Developer))
print(issubclass(Manager, Employee))



# print(dev_1.email)
# print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# print(help(Developer)) # you can see where it inherits from