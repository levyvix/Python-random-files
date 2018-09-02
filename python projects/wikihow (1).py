#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import wikipedia
wikipedia.set_lang('pt')
nomedorobo = "\033[1m\033[34mPandora\033[0;0m» "
nomedapessoa = "\033[1m\033[33mLevy\033[0;0m» "
fim=False
def sair():
    print(nomedorobo + "Deseja sair ?")
    saida = input(nomedapessoa)
    if saida.lower().startswith("s"):
        return 1
    elif saida.lower().startswith("n"):
        return 0

def ajudar():
    print(nomedorobo + "Posso ajudar em mais alguma coisa?")
    saida = input(nomedapessoa)
    if saida.lower().startswith("s"):
        return 1
    elif saida.lower().startswith("n"):
        return 0


while(fim == False):

    mensagem = input(nomedapessoa)
    alo = mensagem.split("é")

    try:
        print (nomedorobo+wikipedia.summary(alo[1], sentences=1))
    except:
        print("Desculpe nao sei o que isso significa!")

    print(nomedorobo+"Deseja saber mais sobre isso ?")
    sorn = input(nomedapessoa)
    if sorn.lower().startswith("s"):
        alo = wikipedia.page(alo[1], )
        print(nomedorobo+alo.content)
        if ajudar():
            print(nomedorobo+"O que deseja saber ?")
            continue
        else:
            if sair():
                fim=True
            else:
                continue
    elif sorn.lower().startswith("n"):
        if ajudar():
            print(nomedorobo + "O que deseja saber ?")
            continue
        else:
            if sair():
                fim=True
            else:
                continue

print(nomedorobo,"Espero ter ajudado! Até Logo!")