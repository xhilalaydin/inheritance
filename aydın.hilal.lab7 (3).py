# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 09:08:30 2023

@author: hilala-ug
"""

class Employee(object):

    def __init__(self , emp_name ,wage, id_num, tax_rate=0.3):
        self.__tax_rate = tax_rate
        self.__emp_name = self.setName(emp_name)
        self.__id_num = self.setId(id_num)
        self.__wage = self.setWage(float(wage))
        #self.setId(id_num)
       
    def getName(self):
        return self.__emp_name

    def getId(self):
        return self.__id_num

    def getWage(self):
        return self.__wage

    def getTaxrate(self):
        return self.__tax_rate
    
    def setTaxrate(self, tax_rate):
        self.__tax_rate = tax_rate
        
    def setName(self, name):
       cleanedName = ""
       for ch in name:
          if (("a"<= ch <= "z") or("A"<= ch <= "Z") or ch ==" "):
              cleanedName += ch 
       return cleanedName

    def setId(self, id_num):
        try:
            integer_id = int(id_num)
        except ValueError:
            integer_id = 11111111
        return integer_id

    def setWage(self, wage):
        if wage < 0:
            wage = 0
        return wage

    def calculateSalary(self):
        tax = self.__wage * self.__tax_rate
        salary = self.__wage - tax
        return salary

    def __lt__(self, other):
        self_parts = self.__emp_name.split()
        other_parts = other.getName().split()

        self_surname = self_parts[-1]
        other_surname = other_parts[-1]
        self_first_name = self_parts[0]
        other_first_name = other_parts[0]

        if self_surname == other_surname:
            return self_first_name < other_first_name
        else:
            return self_surname < other_surname

    def __eq__(self, other):
        if isinstance(other, self.__id_num):
            return self.__id_num == other.getId()

    def __repr__(self):
        return f"Name: '{self.__emp_name}', Employee ID : {self.__id_num}, Wage: {self.__wage}"
    
    
#print(Employee("Kemal Or/an", 57000, 67527))

"""
Create a subclass of Employee, Manager, with the following data members and
methods. Note all data members should be private (__).
Data Members:
● bonus: the bonus of the Manager (float).
Methods:
● __init()__: takes the employee name, id number, wage, and bonus.
Calls the Employee init, to initialize the inherited data members, and sets
the bonus to the value passed as a parameter.
● Get method for bonus.
● calculate_salary(): returns the salary of the manager. Managers
make 10% extra salary in addition to the bonus than a regular employee.
They also pay tax at the same rate.
● __repr()__: returns a string representation of a Manager object. The
method should call the Employee __repr__ to get the Employee data, and
append the Manager data, formatted as shown in the sample run.
"""
class Manager(Employee):
    def __init__(self,emp_name, wage, id_num ,bonus):
        super().__init__(emp_name, wage, id_num )
        self.__bonus = bonus
        
    def getBonus(self):
        return self.__bonus
    
    def calculate_salary(self):
        base_salary = Employee.getWage(self)
        manager_salary = float(base_salary)*1.1 + float(self.__bonus)
        tax_rate= 0.3
        manager_salary = manager_salary - (tax_rate* manager_salary)
        return int(manager_salary)
    
    def __repr__(self):
        employee_data = super().__repr__()
        manager_data = f" Bonus : {self.__bonus}"
        total_data = employee_data + manager_data 
        return total_data 
    
#print(Manager("Ali Aksu",70000, 49822, 5000)) 
    
Employees = []
id_list = []

def read_employees():
    handle = open("employees (1).txt","r")
    for line in handle:
        listo = line[:-1].split(",")
        if listo[0] == "E":
            if (listo[2] not in id_list): 
                Employees.append(Employee(listo[1], listo[3], listo[2]))
                id_list.append(listo[2])
            else:
                print("Duplicate employee id:")
                print(Employee(listo[1], listo[3], listo[2]))
                print("not added")
        else:
            if (listo[2] not in id_list): 
                Employees.append(Manager(listo[1], listo[3], listo[2],listo[4]))
                id_list.append(listo[2])
            else:
                print("Duplicate employee id:")
                print(Manager(listo[1], listo[3], listo[2],listo[4]))
                print("not added")
    return Employees

a = read_employees()
a.sort()


"""   
The script should do the following:
o Get a list of Employees from the file employees.txt, using the function
defined above.
o Sort the list of Employees.
o Display the sorted list of Employees.
o Display the calculated salary of all Employees.
o Display the average calculated salary for Managers.
"""

print("Sorted list : \n [")
for elm in a:
    print(elm)
print("]")
print()

print("Salary of all employees: ")
for elm in a :
    if isinstance(elm, Employee):
        if type(elm) == Employee:
            print(f"{elm.setName(elm.getName())} salary aftertax: {elm.calculateSalary()}")
        if type(elm) == Manager:
            print(f"{elm.setName(elm.getName())} salary aftertax: {elm.calculate_salary()}")
count = 0
salary = 0

for elm in a:
    if type(elm) == Manager:
        count +=1
        print(elm.calculate_salary())
        salary += elm.calculate_salary()
       
        
avg= salary / count
print()
print(f"Average salary for Managers : {avg}")




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    