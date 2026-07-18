# class Dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def sit(self):
#         print(self.name,'is sitting')
#
# my_dog=Dog('Bob',5)
# my_dog.sit()
# print(my_dog.name,'is',my_dog.age)
# your_dog=Dog('bbs',50)
# your_dog.sit()
# print(your_dog.name,'is',your_dog.age)

class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_description(self):
        return f"{self.make} {self.model} {self.year}"

    def update_reading(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the car")

    def increment_odometer(self,miles):
        self.odometer_reading +=miles

    def read_odometer(self):
        print(self.odometer_reading,'mile')

# my_car=Car("Ford","Mustang",2020)
# # my_car.odometer_reading=10
# my_car.update_reading(150)
# my_car.update_reading(100)
#
# print(my_car.get_description())
# my_car.read_odometer()
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size = 40

    def describe_batter(self):
        print(f"{self.battery_size}-kwh")

my_leaf=ElectricCar('byd','han','2020')
print(my_leaf.get_description())
my_leaf.describe_batter()