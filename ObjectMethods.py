class Myclass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfun(self):
        print("Hello my name is "+self.name)
        print("mt age is ", self.age)


p1 = Myclass('rushi', 23)
p1.myfun()
del p1.age
