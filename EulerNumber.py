import sys

term = {}
def  factorial(number):
    if number < 2:
        return 1
    if number not in term:
        term[number] = number*factorial(number - 1)
    return term[number]

n = int(input())

sum = float(0)
for i in range(n+1):
    sum += (1/factorial(i))

print(sum)

