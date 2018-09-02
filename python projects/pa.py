def pa(n,pt):
    i=0
    while i < n:
        print(pt, end=' ')
        pt += rz
        i+=1
    print('\n')

pt = int(input('primeiro termo: '))
rz = int(input('razao da pa: '))
i=0
n=10
print("10 primeiros termos da PA de razao",rz)
pa(n,pt)

while 1:
    n = int(input('Deseja mostrar mais quantos termos: '))
    if(n > 0):
        pa(n, pt)
    else: break