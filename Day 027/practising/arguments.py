# alla on annettu default-arvot muuttujille
def my_function(a=1, b=2):
    print(a)
    print(b)
    print("\n")

my_function()               # 1,2
my_function(5)               # 5,2
my_function(b=4, a=3)         # 3,4
my_function(b=4)               # 1,4





# unlimited positional arguments:   *args

def add(*args):
    print(args)
    for number in args:
        print(number)


add(1, 2)
add(1, 2, 3, "JEE!")

# keyword arguments kwargs:


def special(AAA=666, **kwargs):
    print(AAA, kwargs)
    for key, value in kwargs.items():
        print(key, value)


special(a=3, f=3)
special(333333, XXX="www")


class Car:
    def __init__(self, **kwargs):
        #self.type = kwargs["type"]
        #self.color = kwargs["color"]
        self.type = kwargs.get("type")      # ei crashaa!!!
        self.color = kwargs.get("color")

my_car = Car(type="FIAT", color="RED")
print(my_car.type, my_car.color)
my_car2 = Car()
print(my_car2.type, my_car2.color)

