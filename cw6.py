# Task 1
#
import calculator

val1, val2 = int(input("Input value 1: ")), int(input("Input value 2: "))
operation = input ("Choose operation ('+','-','*','/'): ")
if operation == '+':
    print(val1,operation,val2,"=",calculator.my_sum(val1,val2),sep='')
elif operation == '-':
     print(val1,operation,val2,"=",calculator.my_diff(val1,val2),sep='')
elif operation == '*':
    print(val1,operation,val2,"=",calculator.my_mult(val1,val2),sep='')
elif operation == '/':
    print(val1,operation,val2,"=",calculator.my_div(val1,val2),sep='')
else:
    print("Wrong operation")
input("Press any key")

# Task 2
#
import random

secret_value = random.randint(1,100)
your_value = int(input("Try to guess a number (from 1 to 100): "))
while True:
    if your_value == secret_value:
        print("Great! You are right! Secret number is {}".format(secret_value))
        break
    your_value = int(input("You are wrong. Try again. Input a lower number: " 
        if your_value > secret_value else "You are wrong. Try again. Input a lager number: "))

# Task 3
#
from areas import restangle_area as restan
from areas import right_triangle_area as trian
from areas import circle_area as circ

while True:
    fig = int(input('Input (1-restangle, 2-triangle, 3-circle, 0-exit): '))
    if fig == 1:
        print("Restangle area is {:.2f}".format(restan(float(input("Input lenght: ")),
        float(input("Input width: ")))))
    elif fig == 2:
        print("Right triangle area is {:.2f}".format(trian(float(input("Input height: ")),
        float(input("Input base: ")))))
    elif fig == 3:
        print("Circle area is {:.2f}".format(circ(float(input("Input radius: ")))))
    else:
        break
