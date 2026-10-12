num= int(input("enter the number "))
if num<0 or (num % 10 == 0 and num != 0):
    print("the number is not palindrom")
else:
    original = num
    reversed_num= 0

    while (original>reversed_num):
        digit= original % 10
        reversed_num= (reversed_num*10) + digit
        original//=10
    if original == reversed_num or original == reversed_num // 10:
        print("the number is palindrome")
    else :
        print("the number is not palindrome")