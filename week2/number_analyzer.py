collection=[]
total = 0
count_even = 0
for i in range (10):
    num=int(input("enter a number "))
    collection.append(num)
    total+=num
    if num%2 == 0:
        count_even+=1
collection.sort()
largest_num= collection[9]
lowest_num= collection[0]
average=total/10
count_odd=10-count_even
print(f"largest_num {largest_num}")
print(f"lowest_num {lowest_num}")
print(f"total sum {total}")
print(f"average {average}")
print(f"number of even number {count_even}")
print(f"number of odd numbers {count_odd}")

