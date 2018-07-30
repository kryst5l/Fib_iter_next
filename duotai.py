class Dog(object):
    def talk(self):
        print("汪汪汪")


class Cat(object):
    def talk(self):
        print("喵喵喵")


class Pig(object):
    def talk(self):
        print("嗡嗡嗡")


class Bird(object):
    def talk(self):
        print("叽叽喳喳")


def print_talk(obj):
    obj.talk()


d=Dog()
c=Cat()
p=Pig()
b=Bird()

print_talk(d)
print_talk(c)
print_talk(b)
print_talk(a)

