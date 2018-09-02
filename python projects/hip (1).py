import math
cat1=float(input("comprimento do cateto oposto: "))
cat2=float(input("comprimento do cateteo adjacente:"))

hip= math.pow(cat1,2)+math.pow(cat2,2)

print("hipotenusa: {:.2f}".format(math.sqrt(hip)))