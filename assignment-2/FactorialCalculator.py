n=int(input("Enter number:"))
if n<=0:
    print("Not valid")
    exit()
fact=1
exp="*"
if n==1:
    print(f"factorial is :{fact}")
else:
    for i in range(n,0,-1):
        fact=fact*i
        exp+=str(i)
        if i!=1:
            exp+="*"
        print(f"{i}")
    print(f"{n}!={exp}={fact}")