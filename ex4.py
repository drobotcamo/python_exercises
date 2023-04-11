# list out all divisors of a number:

queryNumber = int(input("Please enter a number, and its divisors will be returned: \n"))
divisors = []

for x in range(1, queryNumber + 1):
    if queryNumber % x == 0:
        divisors.append(x)

print(divisors)