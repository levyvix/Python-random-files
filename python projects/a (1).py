#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os, wikipedia

#Definindo algumas coisas
nomedorobo = '\033[1m\033[34mPandora\033[0;0m» '
nomedapessoa = '\033[1m\033[33mLevy\033[0;0m» '
wikipedia.set_lang('ptbr')

#Variaveis usadas:
sairprograma = False
respondido = False
respostaanterior = '0'

while sairprograma == False:
    mensagem = input(nomedapessoa)

    if mensagem.lower().startswith('o que é') or mensagem.lower().startswith('pesquisa para mim o que é') or mensagem.lower().startswith('pesquisa pra mim o que é') or mensagem.lower().startswith('pesquisa para mim o que significa') or mensagem.lower().startswith('pesquisa pra mim o que significa') or mensagem.lower().startswith('o que significa'):
        if mensagem.lower().startswith('o que significa') or mensagem.lower().startswith('pesquisa para mim o que significa') or mensagem.lower().startswith('pesquisa pra mim o que significa'):
            pesquisar = mensagem.split('significa')
        else:
            pesquisar = mensagem.split('é')

            pesquisanowiki = wikipedia.summary(pesquisar[1],sentences=2)
            print(nomedorobo+pesquisanowiki)
            print(nomedorobo+'Deseja saber mais sobre isso?')
            respondido = True
            sorn = input(nomedapessoa)
            if sorn.lower().startswith('s') or sorn.lower().startswith('q') or not sorn.lower().startswith('s') and not sorn.lower().startswith('n'):
                pesquisanowiki = wikipedia.summary(pesquisar[1], 99999999999999999999999)
                print(nomedorobo+pesquisanowiki)
                continue
            elif sorn.lower().startswith('n'):
                continue

    elif mensagem.lower() == 'limpe a tela':
        os.system('clear')
        respondido = True
        continue

    elif mensagem.lower() == 'pandora':
        print(nomedorobo+'Eu! Posso ajudar?')
        respondido = True
        continue

    ####### BUSCA PELA PALAVRA DIGITADA #######
    arq = open('cvnsbot.txt', 'rb')
    for linha in arq.readlines():
        #Formatar texto
        mensagemdoarq = linha.strip().decode()
        mensagemdoarq = mensagemdoarq.split('»')
        try:
            if mensagem.lower() == mensagemdoarq[0] and respostaanterior.find('?') >= 0 and respostaanterior == mensagemdoarq[2]:
                print(nomedorobo+mensagemdoarq[1].capitalize())
                respostaanterior = mensagemdoarq[1]
                respondido = True
                break
            elif mensagem.lower() == mensagemdoarq[0] and respostaanterior.find('?') <= 0:
                print(nomedorobo+mensagemdoarq[1].capitalize())
                respostaanterior = mensagemdoarq[1]
                respondido = True
                break
            else:
                respondido = False
        except IndexError:
            continue
    arq.close()

    ####### VERIFICAR SE JA FOI RESPONDIDO #######
    if respondido == False and respostaanterior.find('?') >= 0:
        print(nomedorobo+'Não consegui entender :c Poderia me ensinar uma resposta? [S/n]')
        sorn = input(nomedapessoa)
        if sorn.lower() == 's':
            print(nomedorobo+'Como posso responder?')
            respostanova = input(nomedapessoa)
            arq = open('cvnsbot.txt', 'a')
            arq.writelines(mensagem.lower()+'»'+respostanova.lower()+'»'+respostaanterior.lower()+'\n')
            arq.close()
            os.system('clear')
            respostaanterior = '0'
        elif sorn.lower() == 'n':
            continue
        else:
            continue

    elif respondido == False and respostaanterior.find('?') <= 0 :
        print(nomedorobo + 'Não consegui entender :c Poderia me ensinar uma resposta? [S/n]')
        sorn = input(nomedapessoa)
        if sorn.lower() == 's':
            print(nomedorobo + 'Como posso responder?')
            respostanova = input(nomedapessoa)
            arq = open('cvnsbot.txt', 'a')
            arq.writelines(mensagem.lower() + '»' + respostanova.lower() + '\n')
            arq.close()
            os.system('clear')
            respostaanterior = '0'
        elif sorn.lower() == 'n':
            continue
        else:
            continue
