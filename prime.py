a = 0
count = 0

n = int(input("Enter the number to check prime\n"))
a = n//2

for i in range(2, a+1):
    if(n % i == 0):
        print("The given number is not prime")
        count = 1
        break

if(count == 0):
    print("The number is prime")
