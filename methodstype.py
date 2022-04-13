class Company:

    Brand = 'Online'

    def __init__(self,Name,Type,NoOfEmployees):
        self.Name = Name
        self.Type = Type
        self.NoOfEmployees = NoOfEmployees
        #self.Emp = self.Employees('Tarun',6000,8)


        #self.emp = self.Employees()

    #def factorial(self,n):
     #   return self.n * (factorial(self.n - 1))


    def showCompanyInfo(self):
        print("Company name is: ", self.Name, 'Type is: ', self.Type, 'Number of Employees: ', self.NoOfEmployees)

    def get_Name(self):
        return self.Name
    def get_NoOfEmployee(self):
        return self.NoOfEmployees

    def set_Name(self,Value):
        self.Name = Value

    def set_NoOfEmployees(self,Value):
        self.NoOfEmployees = Value


    @classmethod
    def website(cls):
        return cls.Brand

    class Employees:

        def __init__(self,Name,Salary,Experience):
            self.Name = Name
            self.Salary = Salary
            self.Experience = Experience

        @staticmethod
        def nothing():
            print("This is a static method")


        def showEmployeeInfo(self):
            print('Name of the Employee: ', self.Name,'Salary is: ', self.Salary,'Experinece is: ', self.Experience)


C1 = Company('Amazon','E-commerce',10000)
C2 = Company('Tesla','Manufacturing',500)

E1 = Company.Employees('Tarun', 75000, 5)
#Emp1 = C1.Emp.showEmployeeInfo()

#E1.showEmployeeInfo()

C1.showCompanyInfo()

Company.website()

Company.Employees.nothing()


C1.get_Name()
print(C1.Name)

C1.set_Name('LOL')

print((C1.Name))

C2.set_NoOfEmployees(8000)

C2.showCompanyInfo()

print(C1.Brand)

print(Company.website())