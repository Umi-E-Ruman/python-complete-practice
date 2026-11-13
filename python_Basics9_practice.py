
#Range(Give you value within that specific range )
print(range(5))
num=range(6)
print(num)
#range syntax
# Start is  0 by default and step is  by default 1 you skip it it will take default value 
# stop is must value you have to pass it (it is not included means range(5) will from 0 to 4
range(start=1,stop=5,step=1)
# Loops(iteration when we have to repeat something)

#while loop (Example :1)
i=1
while i<=5:
    print(i)
    i+=1
print("Out of the loop")

#while loop (infinite loop no stopping condition)
#while i<=5:
    #print(i)
#while loop (Example :2)
i=1
while i<=5:
    print(i*"*")
    i+=1
print("End!!")

#while loop (Example :3)
i=5
while i>=1:
    print(i* "*")
    i-=1
print("End!!")
# for loop (Example:1)
for i in range(6):
    print(i)
print("End!!")

# for loop (Example:2)
for i in range(1,6):
    print(i)
print("End!!")
print("Even numbers from 1 to 10 :")
for i in range(0,11,2):
    print(i)
print("End!!")








  






