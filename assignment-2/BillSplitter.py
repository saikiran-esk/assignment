TotalBill=int(input("Enter total Bill:"))
people=int(input("Enter number of people:"))
TaxPercentage=int(input("Enter percentage of Tax:"))
TipPercentage=int(input("Enter tip percentage:"))
tax=TotalBill*(TaxPercentage)/100
Aftertax_total=TotalBill+tax
tip=Aftertax_total*(TipPercentage)/100
Aftertip_total=Aftertax_total+tip
Perperson=Aftertip_total/people
print("=== BILL BREAKDOWN===")
print(f"Subtotal: ₹{TotalBill}")
print(f"Tax({TaxPercentage}%): ₹{tax}")
print(f"After tax: ₹{Aftertax_total}")
print(f"tip({TipPercentage}): ₹{tip}")
print(f"total: ₹{Aftertip_total}")
print(f"Per Person :  ₹{Perperson}")

