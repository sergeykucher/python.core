# Task 1
#
def average (*args):
    ''' Function returns average'''
    return sum(args)/len(args)
values = [3,7,3,9,0,-4,34,6,21]
print ("Average of {} is {:.2f}".format(values,average(*values)))

# Task 2
#
def module(val):
    ''' Function returns module'''
    return (val) if val > 0 else (-val)

value = 4
print ("Module of {} is {}".format(value,module(value)))
value = -5
print ("Module of {} is {}".format(value,module(value)))

# Task 3
#
def max_value(val1,val2):
    ''' Function returns max of 2 numbers'''
    return(val1) if val1 > val2 else (val2)

value1 = 4
value2 = 7
print ("From {} and {} max is {}".format(value1,value2,max_value(value1,value2)))
value1 = 4
value2 = -5
print ("From {} and {} max is {}".format(value1,value2,max_value(value1,value2)))

# Task 4
#
def restan(val1,val2):
    '''Function returns restangle area'''
    return val1*val2
def trian(val1,val2):
    '''Function returns triangle area'''
    return val1*val2/2
def circ(val):
    '''Function returns circle area'''
    return val*3.14**2

while True:
    fig = int(input('Input (1-restangle, 2-triangle, 3-circle, 0-exit): '))
    if fig == 1:
        print("Restangle area is {:.2f}".format(restan(float(input("Input lenght: ")),
        float(input("Input width: ")))))
    elif fig == 2:
        print("Triangle area is {:.2f}".format(trian(float(input("Input height: ")),
        float(input("Input base: ")))))
    elif fig == 3:
        print("Circle area is {:.2f}".format(circ(float(input("Input radius: ")))))
    else:
        break

# Task 5
#
def sum_digits(value):
    ''' Function returns sum of digits'''
    result = 0
    while value:
        result += value % 10
        value = value // 10
    return result

value = 5123
print("Sum of digits of number {} is {}".format(value,sum_digits(value)))
value = 5468455681
print("Sum of digits of number {} is {}".format(value,sum_digits(value)))
value = 1507462365681
print("Sum of digits of number {} is {}".format(value,sum_digits(value)))