def solution(number):
    return sum ([value for value in range(1,number) if not value % 3 or not value %5])