n = int(input('Numero de notas: '))
notas = 0
i=0

while i<n:
    notas += float(input("nota: "))
    i+=1



print('a media das notas é {:.1f}'.format(notas/n))