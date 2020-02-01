class xas1:
    pass
m1  = xas1()

class xas2:
    pass
m2  = xas2()

class xas3:
    pass
m3  = xas3()

class xas4:
    pass
m4  = xas4()

# to create a new class

       
class Employee:
   'Common base class for all employees'
   empCount = 0

   def init(self, name, salary): ## to be publica o privada "__init__"
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

"This would create first object of Employee class"      
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)

emp3 = Employee("Jorge", 25000)
emp4 = Employee("xavier", 15000)
emp3.displayEmployee()
emp4.displayEmployee()

emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)




class Employee:
   'Common base class for all employees'
   empCount = 0

   def init(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

print ("Employee.doc:", Employee.doc)
print ("Employee.name:", Employee.name)
print ("Employee.module:", Employee.module)
print ("Employee.bases:", Employee.bases)
print ("Employee.dict:", Employee.dict)












