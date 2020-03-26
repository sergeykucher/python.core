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
