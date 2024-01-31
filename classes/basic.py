class employ:
    increament = 2
    empno = 0
    def __init__(self,name,languages,salery):
        self.emp_name = name
        self.emp_lang = languages
        self.emp_salery = salery
        employ.empno +=1
    def increasse(self):
        self.emp_salery = self.emp_salery * employ.increament

emp1 = employ("aman", "python", 240000)
print("no.of employ",employ.empno)

emp2 = employ("dherrendra","sql", 500000)
print(emp2.emp_lang, emp2.emp_salery,)
print("no.of employ",employ.empno)

emp2.increasse()
print(emp2.emp_lang, emp2.emp_salery)

emp2.increasse()
print(emp2.emp_lang, emp2.emp_salery)
