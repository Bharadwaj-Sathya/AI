# poly Many Morph Form

# 1. Duck Typing
# 2. Operator Overloading
# 3. Method Overloading
# 4. Method Overriding

x = 5
print(id(x))
x = 'Navin'
print(id(x))


class Pycharm:
    def execute(self):
        print("Running")


class Intellij:
    def execute(self):
        print("New IDE")


class Laptop:
    def code(self, ide):
        ide.execute()


# ide = Pycharm()
# laptop1 = Laptop()
# laptop1.code(ide)
# ide =Intellij()
# laptop1.code(ide)

# 2. Operator Overloading
a= 5
b = "String"
print(a+b)