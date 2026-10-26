# Type casting(programmer do explicitly)
#input will taken in string we have to convert it 
age=int(input("Enter your age:"))
print("The age is :" ,age)
age+=1
print("The age after one year is :" ,age)
age=input("Enter your age:")
age=int(age)
#age after one year
age+=1
print("The age after one year is :" ,age)
# Type conversion(compiler so implicitly)
print(30+52.2)

# Sum of two numbers
number_1=int(input("Enter your number 1:"))
number_2=int(input("Enter your number 2:"))
sum=number_1+number_2
print("The number 1 value is ",number_1)
print("The number 2 value is ",number_2)
#  method 1
print("The Sum of two numbers",number_1 ," and " ,number_2, " is " ,sum)

# method 2 (most preferred)
print(f"The sum of two numbers {number_1} and {number_2} is {sum}") 











