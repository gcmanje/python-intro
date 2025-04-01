# inheritance
class Person:
    def __init__(self, name: str, age: int):
        self.name = name.capitalize()
        if age > 100:
            raise Exception("Age cannot be over 100 years")

        self.age = age

    def print_details(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")


# p1=Person("JOHN", 90)
# p1.print_details()

class Student(Person):
    def __init__(self, name: str, age: int, courses: list, adm_number: str):
      super().__init__(name, age)
      print(f"courses:{courses}")
      print(f"adm_number:{adm_number}")

s1 = Student("malia", 90,["Maths","Geo"],"ADM100")
s1.print_details()
