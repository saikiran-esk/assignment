def factorial(n):
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
def is_prime(n):
    if n<=1:
        return "Not Prime"
    elif n==2:
        return "Prime"
    else:
        for i in range(2,n):
            if n%i==0:
                return"Not Prime"
        else:
            return "Prime"
def fibannoci(n):
    if n<=1:
        return n
    return fibannoci(n-1)+fibannoci(n-2)
def sumofdigits(n):
    total = 0
    while n > 0:
        rem = n % 10
        total = total + rem
        n = n // 10
    return total
def reverse_number(n):
    rev=0
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n=n//10
    return rev
def is_armstrong(n):
    temp=n
    total=0
    while temp>0:
        digit=temp%10
        total=total+digit**3
        temp=temp//10
    if total==n:
        return"Armstrong"
    else:
        return"Not Armstrong"
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def lcm(a,b):
    i=1
    while True:
        if i%a==0 and i%b==0:
            return"LCM is:",i
            break
        i=i+1
def is_perfect_number(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    if sum==n:
        return "Perfect number"
    else:
        return "Not perfect"

def menu_functions():
    while(True):
        print("\n menu functions")
        print("1.Factorial")
        print("2.prime checker")
        print("3.Fibannoci term")
        print("4.sum of digits")
        print("5.Reverse number")
        print("6.Armstrong check")
        print("7.GCD")
        print("8.LCM")
        print("9.Perfect NUmber check")
        print("10.Exit")
        ch=int(input("Enter your choice(1-9)"))
        if ch==10:
            print("Exit..")
            exit()
        if ch in [1,2,3,4,5,6,9]:
            n=int(input("Enter Number:"))
        if ch in [7,8]:
            a=int(input("Enter First number:"))
            b=int(input("Enter second number:"))
        match ch:
            case 1:
                result=factorial(n)
            case 2:
                result=is_prime(n)
            case 3:
                result=fibannoci(n)
            case 4:
                result=sumofdigits(n)
            case 5:
                result=reverse_number(n)
            case 6:
                result=is_armstrong(n)
            case 7:
                result=gcd(a,b)
            case 8:
                result=lcm(a,b)
            case 9:
                result=is_perfect_number(n)
        print(f"Result:{result}")
    else:
        print("Invalid choice try agin")
menu_functions()

'''print(factorial(5))
is_prime(5)
print(fibannoci(5))
sumofdigits(132)
reverse_number(132)
is_armstrong(153)
print(gcd(2,3))
lcm(5,3)
is_perfect_number(28)
'''