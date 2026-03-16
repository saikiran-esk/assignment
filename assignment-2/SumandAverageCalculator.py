n=int(input("Enter number of terms:"))
numbers=[]
for i in range(n):
    numbers.append(int(input(f"Enter number{i+1}:")))
sum=0
l=len(numbers)
for i in numbers:
    sum=sum+i
Average=(sum)/l
max=numbers[0]
for i in range(len(numbers)):
    if numbers[i]>max:
        max=numbers[i]
min=numbers[0]
for i in range(len(numbers)):
    if numbers[i]<min:
        min=numbers[i]

print(f"sum={sum}")
print(f"Average is :{Average}")
print(f"Maximum number is :{max}")
print(f"Minimum number is :{min}")