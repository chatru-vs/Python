                                                                    ####Python - OOPS

#class and object

class Computer:
    def config(self):
        print("i5, 16gb, 1TB")

com1 = Computer()
Computer.config(com1)


class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("config is ", self.cpu, self.ram)

com1 = Computer('i5', 16)
com2 = Computer('Ryzen 3', 8)
Computer.config(com1)
Computer.config(com2)
com1.config()
com2.config()

class Computer:
    def __init__(self):
        self.name = "chatrughan"
        self.age = 37

    def update(self):
        self.age = 30


    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False

c1 = Computer()
c2 = Computer()

if c1.compare(c2):
    print("They are same")
else:
    print("They are different")

c1.name = "Rashi"
c1.age = 12
c1.update()
c2.age = 30

print(c1.name)
print(c2.name)

##Instance variable and class variable

class Car:
    wheels = 4

    def __init__(self):
        self.mil = 10
        self.com = "Lamborgini"

c1 = Car()
c2 = Car()

c1.mil = 8
Car.wheels = 5
print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)

#class, static, instance methods

class Student:
    school = 'Python'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    def get_m1(self):
        return self.m1

    def set_m1(self, value):
        self.m1.value

    @classmethod
    def getschool(cls):
        return cls.school
    @staticmethod
    def info():
        print("This is the student class in abc module")

s1 = Student(34,67,32)
s2 = Student(89,56,67)
print(s1.avg())
print(s2.avg())
print(Student.getschool())
Student.info()

# class within class

class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:

            def __init__(self):
                self.brand = 'HP'
                self.cpu = 'i5'
                self.ram = 17
            def show(self):
                print(self.brand, self.cpu, self.ram)


s1 = Student('navin', 4)
s2 = Student('Chatrughan', 56)
s1.show()
lap1 = s1.lap
lap2 = s2.lap
print(id(lap1))
print(id(lap2))

### Inheritance

class A:

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 is working")


class B:
    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")


class C(A, B):
    def feature5(self):
        print("Feature 5 is working")


a1 = A()
a1.feature1()
a1.feature2()

b1 = B()
b1.feature3()
b1.feature4()

c1 = C()
c1.feature5()

### Inheritance Continue

class A:

    def __init__(self):
        print("in A Init")

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 is working")


class B:

    def __init__(self):
        super().__init__()
        print("in B Init")

    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("in C init")


a1 = C()
a1.feature1()
a1.feature4()

## polymorphism - duck typing

class PyCharm:
    def execute(self):
        print("compiling")
        print("running")

class MyEditor:
    def execute(self):
        print("spell check")
        print("convention check")
        print("compiling")
        print("Running")

class Laptop:
    def code(self,ide):
        ide.execute()

ide = PyCharm()
ide = MyEditor()

lap1 = Laptop()
lap1.code(ide)

#Method Overloading

class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)


s1 = Student(56, 78)
s2 = Student(60, 65)

s3 = s1 + s2
print(s3.m1)
print(s1)
print(s2)

# Method overriding

class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a=None,b=None,c=None):
        s = 0
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = a 
        return s

s1 = Student(56, 78)

print(s1.sum(5,7))

# Second Example

class A:
    def show(self):
        print("in A show")
class B(A):
    pass

a1 = B()
a1.show()

