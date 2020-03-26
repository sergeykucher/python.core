# Task 1
print("Task 1")

zen_of_python = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

count_better = len(zen_of_python.split('better'))-1
count_never = len(zen_of_python.split('never'))-1
count_is = len(zen_of_python.split('is'))-1
print('Old style:')
print("Number of 'better' is %d" %count_better)
print("Number of 'never' is %d" %count_never)
print("Number of 'is' is %d" %count_is)
print('New style:')
print ("Number of 'better' is {}".format(count_better))
print ("Number of 'never' is {}".format(count_never))
print ("Number of 'is' is {}".format(count_is))
print('New style 2:')
print (f"Number of 'better' is {count_better}")
print (f"Number of 'never' is {count_never}")
print (f"Number of 'is' is {count_is}")

print(zen_of_python.upper())
zen_of_python = zen_of_python.replace('i','&')
print(zen_of_python)

# Task 2
print("Task 2")

num = 9384

# Mode 1 & Old style
print ("Mode 1 & Old style:")
print ("Number is %d" %num)
num_as_str = str(num)
num_product_of_digits = int(num_as_str[0])*int(num_as_str[1])*int(num_as_str[2])*int(num_as_str[3])
reverse_num = int(num_as_str[3]+num_as_str[2]+num_as_str[1]+num_as_str[0])
sorted_num = int(''.join(sorted(list(num_as_str))))
print ("Product of digits is %d\nReverse number is %d\nSorted number is %d"\
       %(num_product_of_digits,reverse_num,sorted_num))

# Mode 2 & New style
print ("Mode 2 & New style:")
print ("Number is {}".format(num))
num_digits = []
num_digits.append(num//1000)
num_digits.append(num%1000//100)
num_digits.append(num%100//10)
num_digits.append(num%10)
num_product_of_digits = num_digits[0] * num_digits[1] * num_digits[2] * num_digits[3]
print ("Product of digits is {}".format(num_product_of_digits))
num_digits.reverse()
reverse_num = num_digits[0]*(10**3) + \
              num_digits[1]*(10**2) + \
              num_digits[2]*(10**1) + \
              num_digits[3]*(10**0)
print ("Reverse number is {}".format(reverse_num))
num_digits.sort()
sorted_num = num_digits[0]*(10**3) + \
             num_digits[1]*(10**2) + \
             num_digits[2]*(10**1) + \
             num_digits[3]*(10**0)
print ("Sorted number is {}".format(sorted_num))

# Task 3
print("Task 3")

value1 = 23984
value2 = "Some str"

print("Value1 is '{}'\nValue2 is '{}'".format(value1,value2))
value1,value2 = value2,value1
print(f"Value1 is '{value1}'\nValue2 is '{value2}'")