a,b,c=int(input("enter the first number: "),int(input("enter the second number: ")),int(input("enter the third number: ")))

if a>=b and a>=c:
    print("the largest number is:",a)
elif b>=a and b>=c:
    print("the largest number is:",b)
else:
    print("the largest number is:",c)