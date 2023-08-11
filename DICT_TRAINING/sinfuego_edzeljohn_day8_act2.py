class Employee:
    def __init__(self, name, email, phoneNumber):
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber
        
    def __str__(self):
        return "\nName: {} \nEmail: {} \nPhone Number: {}".format(self.name, self.email, self.phoneNumber)


emp1 = Employee("Ej", "edzeljohnsinfuego@gmail.com", "09321654987")
emp2 = Employee("John", "john@gmail.com", "09123456987")

print(emp1, "\n", emp2)