j = input("Please enter your number: ")
sqrt = j**(0.5)
import math
sqrt = math.ceil(sqrt)
sqrt = int(sqrt)
statement = "is a prime number"

for i in range(2,sqrt):
    if i%2!=0:
        if j%i==0:
            statement = "is not a prime number"
            break

print j, statement   
