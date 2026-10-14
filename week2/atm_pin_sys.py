pin= 1234
tries=0
while tries <3:
    attempt = int(input("enter pin "))
    tries+=1
    if pin == attempt:
        print("verification successfull")
        break
    else:
        print(f"Incorrect pin\n Attempts remaining:{3-tries} ")
    