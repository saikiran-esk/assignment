amount=10000
def checkBalance():
    print(amount)
def deposit(money):
    global amount
    amount+=money
    print(f"New balance:{amount}")
def withdraw(money):
    global amount
    if amount-money>=500:
        print("money withdrawn successfully")
        amount-=money
        print(f"Balance:{amount}")
    else:
        print("Insufficient Funds")
        print("Try again")
def main():
    while True:
        print("\n1.check balance\n2.deposit\n3.withdraw\n4.exit")
        print("select the option")
        n=int(input())
        if n==1:
            checkBalance()
        elif n==2:
            money=int(input("Enter amount for deposit: "))
            deposit(money)
        elif n==3:
            money=int(input("Enter the amount for withdraw: "))
            withdraw(money)
        else:
            break
main()
print("Thank you using the ATM")
