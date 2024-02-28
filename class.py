# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)

# class MyClass:
#   x = 5

# p1 = MyClass()
# print(p1.x)









# class Car:
#   def __init__(self,make,model,year):
#     self.make=make
#     self.model=model
#     self.year=year
# def get_age(self):
#   current_year=2023
#   age = current_year-self.year
#   return age
# def display_info(self):
#   return"{self.year}{self.make}{self.model}"
# Car1=Car("toyota","camry",2020)
# print(Car1.display_imp())
# print("Carage:{car1,get_age()} year")



class BankAmount:
    def __init__(self,balance=0):
       self.balance = balance

    def deposite(self,amount):
        if amount>0:
            self.balance +=amount
            def withdraw(self,amount):
                if amount>0 and self.balance>=amount :
                self.balance-= amount
            def get_balance(self):
                return self.balance
    account= BankAccount(1000)
    account.deposite(500)
    account.withdraw(200)
print(f"Amount Balance : {account.get_balance()}")















    9
