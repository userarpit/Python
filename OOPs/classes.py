class Dog:
    attr1 = "mammal"

    def __init__(self,name):
        self.name = name

    def speak(self):
        print("My name is {}".format(Rodger.name))

Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

print("Rodger is a {}".format(Dog.attr1))
print("Tommy is a {}".format(Dog.attr1))

Rodger.speak()
Tommy.speak()

print(type(Rodger))
print(Rodger.__class__)