N=int(input("enter a positive number"))
N=abs(N)
count_even= 0
total=0
for i in range(1,N+1):
    if i % 2==0:
        count_even+=1
    total+=i
count_odd=N-count_even
print(f"number of even number {count_even}")
print(f"number of odd numbers {count_odd}")
print(f"sum of numbers {total}")