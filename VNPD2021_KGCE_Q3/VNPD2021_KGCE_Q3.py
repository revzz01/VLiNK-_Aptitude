#import
import math

#Print Factors of the fiven number
def factors(n):
   print("The factors of",n,"are:")
   for i in range(1, n + 1):
       if n % i == 0:
           print(i)

#Sum of all the even factors
def summation(n) :
   
    res = 1
    for i in range(2, (int)(math.sqrt(n)) + 1) :
          
        count = 0
        summ = 1
        term = 1
        while (n % i == 0) :
            count= count + 1
   
            n = n // i
   
            if (i == 2 and count == 1) :
                summ = 0
   
            term = term * i
            summ = summ + term
          
        result = result * summ
        return result
        print("The sum of the factors is:" ,result)
  
  
# Driver code
#Check for Even Input
n = int(input())
if (num % 2) == 0:
    factors(n)
    summation(n)
    
#Bitwise operator to check odd input
elif n & 1:
    print("You have entered an odd number")
    
#Prime number    
else:
    print("The number you have entered is a prime number, Please input a different number!")
