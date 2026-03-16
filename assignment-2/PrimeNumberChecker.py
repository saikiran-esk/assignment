n=int(input("Enter the number:"))
if n<=1:
    print("Not prime")
else:
    for i in range(2,n):
        if n%i==0:
            print("Not prime")
            break
    else:
        print("prime")
start=int(input("Enter start range:"))
End=int(input("Enter end range:"))

for n in range(start,End+1):
    if n<=1:
        continue
    for i in range(2,n):
        if n%i==0:
            break
    else:
        print(n,end=',')
