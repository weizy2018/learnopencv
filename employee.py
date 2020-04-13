class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    
    def display(self):
        print("name: ", self.name, "  salary: ", self.salary)

    def displayCount(self):
        print("total employee: %d" % Employee.empCount)

    def __del__(self):
        print("destroy")
    
    

emp1 = Employee("zhangsan", 10000)
emp2 = Employee("lisi", 20000)

print(getattr(emp1, 'name'))
setattr(emp1, 'salary', 50000)
print(getattr(emp1, 'salary'))

emp1.display()
emp2.display()
print(Employee.empCount)








    
