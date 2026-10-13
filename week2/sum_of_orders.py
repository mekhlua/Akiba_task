dig=int(input("input the number "))
total=0
while dig > 0:
    digit = dig % 10
    total += digit
    dig //= 10
print("The sum of the digits is:", total)