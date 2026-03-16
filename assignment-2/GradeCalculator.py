English=int(input("Enter English marks out of 100:"))
Hindi=int(input("Enter Hindi marks out of 100:"))
Maths=int(input("Enter Maths marks out of 100:"))
Science=int(input("Enter Science marks out of 100:"))
Social=int(input("Enter Social marks out of 100:"))
TotalMarks=500
MarksObtained=English+Hindi+Maths+Science+Social
Percentage=(MarksObtained/TotalMarks)*100
Grade=("A+","A","B","C","D","F")
print(f"TotalMarks:{MarksObtained}")
print(f"Percentage:{Percentage:.2f}")
if Percentage<50:
    print("Grade:F(Fail)")
elif  50<=Percentage<60:
    print("Grade:D(Pass)")
elif 60<=Percentage<70:
    print("Grade:C(Average)")
elif 70<=Percentage<80:
    print("Grade:B(Good)")
elif 80<=Percentage<90:
    print("Grade:A(Excellent)")
else:
    print("Grade:A+(Outstanding)")
Result=("Pass","Fail")
if(English>=40 and Hindi>=40 and Maths>=40 and Science>=40 and Social>=40):
    print("Result:Pass")
else:
    print("Result:Fail")


    


