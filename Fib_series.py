limit = input("Please enter limit of the series: ")
a = 0
i = 2
Fib = [1,2,3]
sumofmultiples = 0

while a < limit:
    i = i+1
    a = Fib[i-1]+ Fib[i-2]
    Fib.append(a)
    
for j in Fib:
    if j%5 == 0:
        sumofmultiples = sumofmultiples + j
        
print sumofmultiples

