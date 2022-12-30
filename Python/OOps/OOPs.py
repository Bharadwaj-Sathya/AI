# OOPs
# Class
# Objects
# Methods
# Inheritences
# Data Encapsulation
# Polymorphism
# Abstraction

# class

class Computer:
    # Attributes
    # Behaviour

    def __init__(self, processor, ram, storage):
        self.processor = processor
        self.ram = ram
        self.storage = storage
        self.brand = "Computers"

    def config(self):
        print(self.processor, self.ram, self.storage)


# Objects

com1 = Computer('i5', '16gb', '1TB')
com1.config()

com1 = Computer('Ryzn 3600', '8gb', '2TB')
com1.config()


class Car:
    wheels = 4

    def __init__(self):
        self.mil = 10
        self.com = "BMW"


c1 = Car()
print(c1.com, c1.wheels)
Car.wheels = 5
print(c1.com, c1.wheels)


class A:
    def __init__(self):
        print("A init method")

    def feature1(self):
        print("Feature 1 Working")

    def feature2(self):
        print("Feature 2 Working")


class B():
    def __init__(self):
        print("B init method")

    def feature3(self):
        print("Feature 3 Working")

    def feature4(self):
        print("Feature 4 Working")


class C():
    def feature5(self):
        print("Feature 5 Working")

    def feature6(self):
        print("Feature  6 Working")


class D(A, B):
    def __init__(self):
        super().__init__()
        super().__init__()

        print("D init method")

    def feature7(self):
        print("Feature 7 Working")

    def feature8(self):
        print("Feature  8 Working")


# a1 = A()
# a1.feature2()
# b1 = B()
# b1.feature3()
# b1.feature1()
#
# c = C()
# d = D()
# d.feature5()

d2 = D()
