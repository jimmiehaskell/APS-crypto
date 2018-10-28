"""
    O Projeto foi elaborado para o trabalho semestral do curso de Ciência da Computação
    da Unip-DF.
    APS     : Atividade Pratica Supervisionada
    Curso   : Ciência da Computação
    Turmas  : CC1P30 e CC2P30
    Tema    : AS TÉCNICAS CRIPTOGRÁFICAS, CONCEITOS, USOS E APLICAÇÕES
    Campus  : Unip Brasília
    Alunos  : [
                Nome: JIMMIE HASKELL GONÇALVES DA SILVA |   Matrícula: D82BIE-3,
                Nome: DAVIDSON CARLOS DA ROCHA FERREIRA |   Matrícula: N359BB-1,
                Nome: LUDSON ROSENDA DE OLIVEIRA        |   Matrícula: D824AA-8,
                Nome: NORTON JUNIOR MASERA              |   Matrícula: N34943-3,
                Nome: FRANCISCO WANDERSON SOUSA DA SILVA|   Matrícula: N372HF-4
                ]

    Projeto elaborado com informações obtidas na internet através link:
    https://www.lambda3.com.br/2012/12/entendendo-de-verdade-a-criptografia-rsa/
"""
#-*- encoding: utf-8 -*-

import random

#===========================#
# metodos da aplicação RSA  #
#===========================#

# VRF se o número gerado é primo
def primo(numero):
    i = 1
    tempo = 0
    while i <= numero:
        if numero % i == 0:
            tempo = tempo + 1
        i = i + 1

    if tempo == 2:
        return True
    else:
        return False

# Calcula o totient do número primo
def totient(numero):
    if primo(numero):
        return numero - 1
    else:
        return False

# Gera um número aleatório E
# Dentro das condições 1 < E < Phi(N)
def numE(numero):
    def mdc(numero1, numero2):
        while numero2 != 0:
            resto = numero1 % numero2
            numero1 = numero2
            numero2 = resto
        return numero1
    while True:
        e = random.randrange(2, numero)
        if mdc(numero, e) == 1:
            return e

# Gera um número primo aleatório
def gNumPrimo():
    while True:
        x = random.randrange(1, 2**11) # define o tamanho dos números primos. Faixa PADRÃO do RSA = 2**2048
        if primo(x):
            return x

# Faz a MOD (%) entre os números
def mod(numero1, numero2):
    if numero1 < numero2:
        return numero1
    else:
        numero3 = numero1 % numero2
        return numero3

# Cifra o texto
def cifra(fileName, nipKey):
    with open(('txt/' + fileName + '.txt'), 'r', encoding='UTF-8') as f:
        with open(('bin/publicKeys/' + nipKey + '.hsk'), 'r', encoding='UTF-8') as k:
            key = k.readlines()
            keyE = int(key[1])
            keyN = int(key[0])

        with open(('cifrados/' + fileName + '.cif'), 'w') as fileSave:
            for file in f:
                file = list(file)
                tamanho = len(file)
                x = 0
                while x < tamanho:
                    file[x] = ord(file[x])
                    file[x] = file[x]**keyE
                    file[x] = mod(file[x], keyN)
                    file[x] = int(file[x])
                    x = x + 1
                file = str(file).replace("[", "")
                file = str(file).replace(",", "")
                file = str(file).replace("]", "")
                print(file, file=fileSave)
                print(file)
        fileSave.close()
        k.close()
    f.close()
    print("\n")
    print("Arquivo " + fileName + " CIFRADO.\n")

# Decifra o texto
def descifra(fileName, nipKey):
    with open(('cifrados/' + fileName + '.cif'), 'r') as f:
        with open(('bin/privateKeys/' + nipKey + '.phsk'), 'r') as k:
            key = k.readlines()

            keyD = int(key[1])
            keyN = int(key[0])

        with open(('decifrados/' + fileName + '.txt'), 'w', encoding='UTF-8') as fileSave:
            for lista in f:
                lista = lista.split()
                tamanho = len(lista)
                x = 0
                while x < tamanho:
                    lista[x] = int(lista[x])
                    lista[x] = lista[x]**keyD
                    lista[x] = mod(lista[x], keyN)
                    lista[x] = chr(lista[x])
                    lista[x] = lista[x].rstrip("\n")
                    x = x + 1
                lista = str(lista).replace("[", "")
                lista = str(lista).replace("'", "")
                lista = str(lista).replace(", ", "")
                lista = str(lista).replace("]", "")
                print(lista, file=fileSave)
                print(lista)
        fileSave.close()
        k.close()
    f.close()

# Chave privada
def gPrivateKey(totient, e):
    d = 0
    while(mod(d*e, totient) != 1):
        d = d + 1
    return d
