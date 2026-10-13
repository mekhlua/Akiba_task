secret_number= 23
count = 0

for i in range(5):
    gussed_num= int(input("guess the secret number "))
    if gussed_num == secret_number:
        count += 1
        print(f"Congratulations!\nYou guessed the number in {count} attempts.")
        break

else :
        print("Game Over!")
        

