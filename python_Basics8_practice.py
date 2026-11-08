try:
    number_1=float(input("Enter first number: "))
    number_2=float(input("Enter second number: "))
    operator=input("Enter the operator of operation you want to perform:").strip()
    
except ValueError:
    print("Please enter a valid number")
    raise SystemExit
if operator== '+':
    print(f"The sum of two numbers {number_1} and {number_2} is {number_1+number_2}")
elif operator=='-':
    print(f"The difference of two numbers {number_1} and {number_2} is {number_1-number_2}")
elif operator=='*':
    print(f"The multiplication of two numbers {number_1} and {number_2} is {number_1*number_2}")
elif operator=='/':
    if number_2 == 0:
        print("Cannot divide by zero")
    else:
        print(f"The division of two numbers {number_1} and {number_2} is {number_1/number_2}")
elif operator=='//':
    if number_2 == 0:
        print("Cannot divide by zero")
    else:
        print(f"The division of two numbers (Answer in integer) {number_1} and {number_2} is {number_1//number_2}")
elif operator=='%':
    if number_2 == 0:
         print("Cannot divide by zero")
    else:
        print(f"The remainder after division  of two numbers {number_1} and {number_2} is {number_1%number_2}")
elif operator=='**':
    print(f"The power of number {number_1} when  {number_2} is exponent is  {number_1**number_2}")
else:
    print("Not valid operator !!")

    