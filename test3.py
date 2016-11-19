class Employee:
    empcount=0;

    def __init__(self,salary,name,gender):
        self.name = name;
        self.salary = salary;
        self.gender = gender;
        Employee.empcount+=1;

    def count(self):
        print (Employee.empcount);

    def display(self):
        print ('name:',self.name,' salary:',self.salary,' gender:',self.gender);

emp1=Employee(10000,'Jason','M')
emp2=Employee(2000,'Susan','F')
emp3=Employee(5000,'Nelson','M')
emp1.display()
emp2.display()
emp3.display()
print('Number of employees is %d' % Employee.empcount)



