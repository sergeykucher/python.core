# Task 1
#
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
#
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
#
value = int(input("Input value: "))
factorial_value = 1
for i in range(value):
    factorial_value *= i+1
print ("Factorial of {} is {}".format(value,factorial_value))

# Task 4
#
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

# Task 5
#
counter = 1
while True:
    if int(input("Input number {}: ".format(counter))) > 0:
        counter += 1
    else:
        break

# Task 6
#     
list3 = []
num = int(input("Input number of values: "))
for num in range(num):
    value = int(input("Input value {}: ".format(num))) 
    if value > 0:
        list3.append(value)
    else:
        print ("Value is negative or '0'. Stopping input")
        break    

# Task 7
#
list_simples = []
shift = 10
list4 = list(range(shift,31))
print ("Origin list: {}".format(list4))
for value1 in list4:
    for value2 in range (2,value1):
        if not value1%value2:
           list4 [value1-shift] = [value2,value1//value2]
           break 
    else:
        list_simples.append(value1)
print ("List of simple numbers: {}".format(list_simples))
print ("Modified list: {}".format(list4))

# Task 8
#
sentence = "If the implementation is easy to explain, it may be a good idea."
print ("Original sentence: {}".format (sentence))
words = [word for word in sentence.split()]
words.sort(key=len)
print ("Modifies sentence: {}".format(' '.join(words)))