# property decorators: getters, setters, deleters

class Employee:
    raise_amount = 1.04

    def __init__(self, first, last):
        self.first = first  
        self.last = last  

    @property # defined like a method, accessed like an attribute
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None

    
emp_1 = Employee('Jon', 'Smith')

emp_1.first = 'Jim'
emp_1.fullname = 'Billy Bob'

print(emp_1.fullname)
print(emp_1.first)
print(emp_1.email)

del emp_1.fullname
