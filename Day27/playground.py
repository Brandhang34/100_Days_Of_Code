def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print(add(2,3,4,5,6))

def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get["make"]
        self.model = kw.get["model"]

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
