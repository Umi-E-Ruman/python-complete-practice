
try:
    marks = float(input("Enter your Marks: "))
except ValueError:
    print("Please enter a valid number.")
    raise SystemExit
if marks<0 or marks>100 :
    print("Marks does not lies in valid range")
if marks>=90:
    print("Your grade is A")
    print("Exceptional")

elif marks>=80:
    print("Your grade is B")
    print("Good")

elif marks>=70:
    print("Your grade is C")
    print("Average")

elif marks>=60:
    print("Your grade is D")
    print("Need to improve")

else marks>=0:
    print("Your grade is F")
    print("Fail")


  
    

