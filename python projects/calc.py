def soma(a,b):
    return a+b

def sub(a,b):
    return  a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b


print('Digite 2 valores: ')
n = input('')
n = n.split(' ')
while 1:
    print('\n\nEscolha a operaç\ão desejada: ')
    print('[1] - Adição\n[2] - Subtração\n[3] - Multiplicaçao\n[4] - Divisão\n[5] - Sair do programa')
    op = int(input(''))
    if op == 5:
        break
    elif op == 1:
        print("Soma dos valores:", soma(int(n[0]), int(n[1])))
    elif op == 2:
        print("Diferença dos valores:", sub(int(n[0]), int(n[1])))
    elif op == 3:
        print("Produto dos valores:", mul(int(n[0]), int(n[1])))
    elif op == 4:
        print("Razão dos valores:", div(int(n[0]), int(n[1])))