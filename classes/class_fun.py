class student:
    def stu_details(self, id, name, fees):
        self.id = id
        self.name = name
        self.fees = fees

stu1 = student()
stu2 = student()
stu1.stu_details(1,"aman", "2000")
stu2.stu_details(2,"ang", "3000")
# print(student)
# print(stu1.id)

class company(student):
    employ_count = 0
    increment = 2
    def __init__(self, name="name", age=0, salary=0):
        self.empname = name
        self.empage = age
        self.empsalary = salary
        company.employ_count +=1
        self.increment +=1

    def emp_role(self, emp_position, emp_time, emp_experience):
        self.emp_position = emp_position
        self.emp_time = emp_time
        self.emp_experience = emp_experience
        self.increment +=2

    def increase(self):
        self.empsalary = int(self.empsalary * self.increment)

    @classmethod
    def change_increment(cls, amount):
        cls.increment = amount
com4=company()


# print(com4.change_increment(10))
# from class student [inharit]

# print(stu1.id, stu1.name, stu1.fees) 
# print(stu2.id, stu2.name, stu2.fees)
# print(stu1.__dict__)

com1 = company("aman",22,200000)
# print("no.of employ",company.employ_count)

com2 = company("adit",23,30000)
# print("no.of employ",company.employ_count)


print(com1.empage, com1.empname, com1.empsalary, )
# print(com2.empage, com2.empname, com2.empsalary)
com1.increase()
print(com1.increment)
com1.change_increment(10)
com1.increase()
print(com1.increment)
print(com1.empage, com1.empname, com1.empsalary, )


# com3 = company()
# com3.emp_role("python developer"," 12 hours",2)
# print(com3.increment)
# print(com3.emp_position, com3.empsalary, com3.empname, com3.emp_experience, com3.emp_time, com3.employ_count)