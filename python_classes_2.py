# person class
from datetime import date, datetime


class Person:
    def __init__(self, name, dob, gender, disabled):
        self.name = name
        self.dob = dob
        self.gender = gender
        self.disabled = disabled

    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Dob: {self.dob}")
        print(f"Gender: {self.gender}")
        if self.disabled:
            print("Disabled")
        else:
            print("Enabled")
        print("_____________________")

    def get_age(self):
        current_date = datetime.today()
        # 19-11-2005
        date_birth = datetime.strptime(self.dob, "%d-%m-%Y")
        age = current_date - date_birth
        print("Age is:", age.days // 365)


p1 = Person("Zora", "12-07-2006", "female", False)
p2 = Person("tyrone", "12-09-2000", "male", True)

p1.print_details()
p1.get_age()
