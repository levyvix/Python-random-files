def cinco(preco):
    return preco - (preco * 5 / 100)

def dez(preco):
    return preco - (preco * 10 / 100)

def quinze(preco):
    return preco - (preco * 15 / 100)

def vinte(preco):
    return preco - (preco * 20 / 100)

def trinta(preco):
    return preco - (preco * 30 / 100)


p=float(input('Preço: R$'))

f=int(input('Desconto (5%, 10%, 15%, 20%, 30%): '))

if f==5:
    print('Após desconto:',cinco(p))
else:
    if f==10:
        print('Após desconto: R$',dez(p))
    else:
        if f==15:
            print('Após desconto:',quinze(p))
        else:
            if f==20:
                print('Após desconto:',vinte(p))
            else:
                if f==30:
                    print('Após desconto:',trinta(p))
                else:
                    print('Error')
