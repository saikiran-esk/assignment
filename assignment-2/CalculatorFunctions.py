
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "cannot divide by zero"
    else:
        return a/b
def modulus(a,b):
    return a%b
def power(a,b):
    return a**b
def Calculator():
    while(True):
        print("\n calculator options")
        print("1.Addition")
        print("2.Substraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Modulus")
        print("6.power")
        print("7.exit")

        ch=int(input("Enter your choice(1-7):"))
        if ch==7:
            print("Exit")
            exit()
        if ch in [1,2,3,4,5,6]:
            a=float(input("Enter First Number:"))
            b=float(input("Enter Second Number:"))
            match ch:
                case 1:
                    result=add(a,b)
                case 2:
                    result=subtract(a,b)
                case 3:
                    result=multiply(a,b)
                case 4:
                    result=divide(a,b)
                case 5:
                    result=modulus(a,b)
                case 6:
                    result=power(a,b)
            print(f"Result:{result}")
        else:
            print("Invalid choice try again")
Calculator()

                

