# # Task 1
num1, num2 = float(input("Input num1: ")), float(input("Input num2: "))
if num1 < num2:
    print("%.2f < %.2f" %(num1,num2))
elif num1 > num2:
    print("%.2f > %.2f" %(num1,num2))

# # Task 2    
num3 = int(input("Input num3: "))
print ("{} is even".format(num3)) if num3%2 ==0 else print("{} is odd".format(num3))

# Task 3
num4 = int(input("Input num4: "))
factorial_num4 = 1;
for i in range(num4):
    factorial_num4 *= i+1
print (f"Factorial of {num4} is {factorial_num4}")