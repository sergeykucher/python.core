# # Task 1_1

# Напишіть програму, яка пропонує користувачу ввести ціле число і визначає
# чи це число парне чи непарне, чи введені дані коректні.

def is_odd_or_even(num):
    if num % 2:
        print("Input number is odd")
    else:
        print("Input number is even")

try:
    number = int(input("Input number: "))
    is_odd_or_even(number)
except ValueError as ve:
    print("Input number is incorrect. ValueError:", ve)
except Exception as ex:
    print("Input number is incorrect. Exception:", ex)

# Task 1_2

# Напишіть програму, яка пропонує користувачу ввести свій вік, після чого виводить повідомлення
# про те чи вік є парним чи непарним числом. Необхідно передбачити можливість введення від’ємного числа,
# в цьому випадку згенерувати власну виняткову ситуацію.
# Головний код має викликати функцію, яка обробляє введену інформацію.

def print_age_is_odd_or_even(age):
    print("Your age is odd" if age % 2 else "Your age is even")

try:
    age = int(input("Input your age: "))
    if age < 0:
        raise ValueError("Input positive value for age")
except ValueError as ve:
    print (ve)    
except:
    print ("Ooops! Something wrong with your age")
else:
    print_age_is_odd_or_even(age)

# Task 1_3

# Напишіть програму для обчислення частки двох чисел, які вводяться користувачем послідовно через кому,
# передбачити випадок ділення на нуль, випадки синтаксичних помилок та випадки інших виняткових ситуацій.
# Використати блоки else та finally.

def div(num1,num2):
    return num1/num2

while True:
    two_numbers = input("Input 2 float numbers (points allowed) with comma separated (f.e 5.7,7.45) or Enter to exit: ")
    if not two_numbers:
        break
    try:
        numbers = [float(number) for number in two_numbers.split(',')]
        if not len(numbers) == 2:
            raise SyntaxError(f"Found {len(numbers)} float numbers")    
        if not numbers[1]:
            raise ZeroDivisionError("Division by zero")
    except ValueError:
        print ("Input correct numbers")    
    except SyntaxError as se:
        print(se)
    except ZeroDivisionError as zde:
        print(zde)    
    else:
        print(f"Division of {numbers[0]} by {numbers[1]} is {div(numbers[0],numbers[1]):.2f}")
    finally:
        print("Try again")

# Task 1_4

# Написати  програму, яка аналізує введене число та в залежності від числа видає день тижня,
# який відповідає цьому числу (1 це Понеділок, 2 це Вівторок і т.д.).
# Врахувати випадки введення чисел від 8 і більше, а також випадки введення не числових даних.

DAYS = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
try:
    day_of_week = int(input("Input day of the week (from 1 to 7): "))
    if not 0 < day_of_week < 8:
        raise ValueError ("Day of the week out of range")
except ValueError as va:
    print(va)
except Exception as ex:
    print(ex)
else:
    print (f"The day of the week is {DAYS[day_of_week-1]}")

# Task 2_1

# Створити клас машина з атрибутами name,  make, model та методами start та stop,
# які виводять інформацію про те що автомобіль стартував чи зупинився відповідно.

class Car:
    def __init__ (self,name,make,model):
        self.name = name
        self.make = make
        self.model = model

    def start(self):
        print(f"Car {self.name} made by {self.make} model {self.model} starting")

    def stop(self):
        print(f"Car {self.name} made by {self.make} model {self.model} has stopped")    

c1 = Car('BC0001HP','ZAZ-Daewoo','Tavria')
c1.start()
c1.stop()

# Task 2_2

# Створити клас особа,  в якому конструктор встановлює ім’я, а метод info виводить повідомлення
# “Hello, my name is {ім’я конкретного екземпляра класу}”, а також створити клас автомобіль,
# в якому конструктор встановлює ім’я, а метод move виводить повідомлення 
# {ім’я конкретного екземпляра класу}  moves at the speed {speed(цей параметр метод moveотримує як вхідний)} km / h

class Person:
    def __init__(self,name):
        self.name = name
    
    def say_hello(self):
        print(f"Hello, my name is {self.name}")

p1 = Person('Dmytro')
p1.say_hello()

class NewCar:
    def __init__(self,name):
        self.name = name

    def moves(self, speed):
        print(f"Car {self.name} moves at speed {speed} km/h")

nc1 = NewCar('BC0002HP')
nc1.moves(50)

# Task 2_3

# Створити клас особа,  в якому конструктор встановлює ім’я, вік.
# Використати в цьому класі геттери та сеттери, а також створити метод info,
# який виводить інформацію про ім’я та вік особи.
# А тоді створити клас працівник, який наслідується від класу особи і містить метод details,
# який на вхід отримує параметр про компанію, в якій працює працівник і цей метод виводить інформацію про те,
# що працівник з таким то іменем працює в такій то компанії.

class NewPerson:
    def __init__(self,name,age):
        self.__set_name(name)
        self.__set_age(age)

    def __get_name(self):
        return self.__name

    def __set_name(self,name):
        self.__name = name

    def __get_age(self):
        return self.__age

    def __set_age(self,age):
        if age < 0:
            self.__age = 0
        elif age > 120:
            self.__age = 120
        else:
            self.__age = age

    name = property(__get_name,__set_name)
    age = property(__get_age,__set_age)

class Worker(NewPerson):
    def __init__(self,*args):
        super().__init__(*args)
        
    def details(self, company):
        print (f"{self.name} works in {company} company")

w1 = Worker('John', 30)
w1.details('Google')

# Task 2_4

# Створити батьківський клас Figure з методами 
# init: ініціалізується колір,
# get_color: повертає колір фігури,
# info: надає інформацію про фігуру та колір,
# від якого наслідуються такі класи як Rectangle, Square, які мають інформацію про ширину, висоту фігури,
# метод square, який знаходить площу фігури.

class Figure:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def get_color(self):
        return self.color

    def info(self):
        print(f"Figure {self.name} has {self.color} color")

class Rectangle(Figure):
    def __init__(self, name, color, width, height):
        super().__init__(name, color)
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height

class Square(Figure):
    def __init__(self, name, color, side):
        super().__init__(name, color)
        self.side = side

    def square(self):
        return self.side**2

f1 = Figure('Circle', 'PINK')
print(f"{f1.name} has {f1.get_color()} color")
f1.info()

r1 = Rectangle('Rectangle','BLACK',23,11)
r1.info()
print(f"Area of {r1.name} with width={r1.width} and height={r1.height} is {r1.square()}")

s1 = Square('Square','RED',12)
s1.info()
print(f"Area of {s1.name} with side={s1.side} is {s1.square()}")
