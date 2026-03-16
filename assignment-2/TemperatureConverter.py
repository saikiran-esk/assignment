def CelsiusToFahrenheit(C):
    F=(C*(9/5))+32
    print(f"Celsius to Fahrenheit is:{F}F")
def FahrenheitToCelsius(F):
    C=(F-32)*(5/9)
    print(f"Fanhreneit to Celsius is:{C}C")
def CelsiusToKelvin(C):
    K=C+273.15
    print(f"Celsius to Kelvin is:{K}K")
def KelvinToCelsius(K):
    C=K-273.15
    print(f"Kelvin to Celsius is:{C}C")
def FahrenheitToKelvin(F):
    K=(F-32)*(5/9)+273.15
    print(f"Fahrenheit to kelvin is:{K}K")
def KelvinToFahrenheit(K):
    F=(K-273.15)*(9/5)+32
    print(f"Kelvin to Fahreneit is:{F}F")
def menu_functions():
    while(True):
        print("\n Temperature Conversions")
        print("1.Celsius to Fahrenheit")
        print("2.Fahrenheit to Celsius")
        print("3.Celsius to Kelvin")
        print("4.Kelvin to Celsius")
        print("5.Fahrenheit to Kelvin")
        print("6.Kelvin to Fahrenheit")
        print("7.Exit")
        ch=int(input("Enter your choice(1-7):"))
        if ch==7:
            print("Exit...")
            exit()
        if ch in [1,3]:
            C=int(input("Enter temperature in C:"))
        elif ch in [2,5]:
            F=int(input("Enter temperature in F:"))
        elif ch in [4,6]:
            K=int(input("Enter temperature in K:"))
        match ch:
            case 1:
                CelsiusToFahrenheit(C)
            case 2:
                FahrenheitToCelsius(F)
            case 3:
                CelsiusToKelvin(C)
            case 4:
                KelvinToCelsius(K)
            case 5:
                FahrenheitToKelvin(F)
            case 6:
                KelvinToFahrenheit(K)

    
menu_functions()


