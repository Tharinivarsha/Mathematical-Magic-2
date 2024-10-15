#Activity1
from math import sqrt
number=int(input("Enter a number to check if it is prime or not: "))
if number>1:
    for i in range(2,int(sqrt(number))+1):
        if (number%i==0):
            print("The number is not prime",number)
    else :
        print("The number is a prime",number)
else :
    print("The number is not prime",number)