#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import wikipedia
wikipedia.set_lang('pt')
nomedapessoa = ('Levy: ')
sair = False
while(sair == False):
    mensagem = raw_input(nomedapessoa)
    try:
        print (wikipedia.summary(alo[1], sentences=2))
        print("deseja saber mais sobre isso ? ")
        # sorn = raw_input(nomedapessoa)
        # if sorn.lower().startswith("s"):
        #     print(wikipedia.summary(alo[1], sentences=5)