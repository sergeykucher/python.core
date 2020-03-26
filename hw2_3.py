value1, value2 = 23984, "Some str"

print("Value1 is {}\nValue2 is {}".format(value1,value2))
value1,value2 = value2,value1
print(f"Value1 is {value1}\nValue2 is {value2}")