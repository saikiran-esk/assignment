Age=int(input("Enter Age :"))
Dayofweek=input("Enter day of week:")
Numberoftickets=int(input("Enter number of tickets:"))
if Age<3:
    price=0
elif 3<=Age<=12:
    price=150
elif 13<=Age<=59:
    price=300
else:
    price=200
base_price=price*Numberoftickets
if Dayofweek in ["Friday","Saturday","Sunday"]:
    discount=0.20*base_price
else:
    discount=0
final_price=base_price-discount
print("\n ticket")
print(f"Base Price:{base_price}")
print(f"discount:{discount}")
print(f"final price after discount:{final_price}")


