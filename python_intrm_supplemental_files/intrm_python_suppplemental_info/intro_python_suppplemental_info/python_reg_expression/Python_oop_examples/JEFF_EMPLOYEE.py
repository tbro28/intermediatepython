class Employee:
    def __init__(self, lastName, firstName):
        self.lastName = lastName
        self.firstName = firstName
        
    def getLastName(self):
        return self.lastName

    def setLastName(self,newln): 
        ##self.lastName = str(input("Enter Last Name: "))
		self.lastName=newln

    def getFirstName(self):
        return self.firstName

    def setFirstName(self):
        self.firstName = str(input("Enter First Name: "))

    def getName(self):
        name = self.getFirstName() + " " + self.getLastName()
        return str(name)

    def setName(self):
        self.setLastName()
        self.setFirstName()


employee = Employee("Taylor","Jeff")
e1= Employee("Smow","joe")
e1.setLastName("smith")
print("Employee Data")
print("Employee Name: {:s}".format(e1.getLastName()))
print("Employee Name: {:s}".format(employee.getName()))
employee.setLastName()
print("Employee Name: {:s}".format(employee.getName()))
employee.setName()
print("Employee Name: {:s}".format(employee.getName()))
