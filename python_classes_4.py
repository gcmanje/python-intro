from datetime import datetime


#cars
class Cars:
    def __init__(self, make, model, date_of_make,drive_side):
        self.make = make
        self.model = model
        self.date_of_make = date_of_make
        self.drive_side = drive_side

    def print_details(self):
        print(f"Make:{self.make}")
        print(f"Model:{self.model}")
        print(f"Date of make:{self.date_of_make}")
        print(f"Drive side:{self.drive_side}")

    def get_age(self):
        current_date=datetime.today()
        age=current_date- self.date_of_make
        pass



cars1=Cars("Toyota","Corolla","1995","left")
cars1.print_details()