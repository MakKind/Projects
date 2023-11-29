# def add(*args):
#     s = 0
#     for i in args:
#         s += i
#     print(s)
#
#
# add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")
my_car = Car(make="Nissan", model="GT-R", color= "Red", seats= 5)
print(my_car.seats)