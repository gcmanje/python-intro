# Account

class Account:
    def __init__(self, acc_number, name, balance):
        self.acc_number = acc_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit was successful. Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount

    def details(self):
        print(f"Name: {self.name}")
        print(f"Account number: {self.acc_number}")
        print(f"Balance: {self.balance}")
        print("_____________________")
acc1 = Account("001","Tom Hicks",7000)
acc2 =Account("002","Mia Hicks",6500)

acc1.deposit(1000)
acc1.withdraw(200)
acc1.details()



# Car [make,model,date_of_make,drive_side]
# get_age
# allowed_in_kenya
# print details