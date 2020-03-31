# Task 1
num = int(input("Input number of values: "))
list1 = [int(input("Input {} element ".format (i))) for i in range(num)]

# Method 1
list1.sort()
print ("Max number is {}\nMin number is {}".format(list1[-1],list1[0]))

max = list1[0]
min = list1[0]
for value in list1:
    if value > max:
        max = value
    if value < min:
        min - value    
print ("Max number is {}\nMin number is {}".format(max,min))

# Task 2
list2 = list(range(1,11))

print ("Even values dividing on '2' are:",end='')
for value in list2:
    if not value % 2:
        print(" {}".format(value),end='')
print()
print ("Odd values dividing on '3' are:",end='')
for value in list2:
    if value % 2 and not value % 3:
        print(" {}".format(value),end='')
print()
print ("Values which don't divide on '2' and '3' are:",end='')
for value in list2:
    if value % 2 and value % 3:
        print(" {}".format(value),end='')
print()

# Task 3

value = int(input("Input value: "))
factorial_value = 1;
for i in range(value):
    factorial_value *= i+1
print ("Factorial of {} is {}".format(value,factorial_value))

# Task 4
while True:
    user_login = input("Login ('enter' to exit):")
    if user_login == '':
        print ("Good bye")
        break
    elif user_login == 'First':
        print ("Hello, First")
        break
    else:
        print ("Login incorrect")    