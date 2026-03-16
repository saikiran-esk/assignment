s=input("Enter Word/Number:")
rev=""
for i in s: 
        rev=i+rev
print(f"Original :{s}")
print(f"Reversed :{rev}")
if s.lower()==rev.lower():
        print("Result :Palindrome")
else:
    print("Result :Not Palindrome")
        
