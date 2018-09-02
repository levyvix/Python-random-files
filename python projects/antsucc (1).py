import random

n = random.randint(1, 10)
#print(n)
n1 = 0
n1 = int(input("Numero: "))
while n1!=n:
    print("Erou!")
    n1 = int(input("Numero: "))

print("Acertou!")
