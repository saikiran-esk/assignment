print("choose pattern")
print("1.Increasing Numbers")
print("2.Repeated Row Numbers")
print("3.Reverse decreasing")
print("4.Pyramid Pattern")
ch=int(input("Enter your choice(1-4):"))
if ch<1 or ch>4:
    print("Invalid choice")
    exit()
n=int(input("Enter height:"))
if ch==1:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
elif ch==2:
    for i in range(1,n+1):
        for j in range(i):
            print(i,end=" ")
        print()
elif ch==3:
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print(j,end=" ")
        print()
elif ch==4:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        for j in range(i-1,0,-1):
            print(j,end=" ")
        print()
else:
    print("invalid choice")

