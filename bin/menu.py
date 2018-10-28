#-*- encoding: utf-8 -*-
from . import methods
import os

def main():

    print("\nInforme o valor correspondente a operação que deseja realizar:\n")
    print("[1] - Criar Chave Publica / Privada.")
    print("[2] - Cifrar uma mensagem.")
    print("[3] - Decifrar uma mensagem.")
    print("[0] - Para sair do sistema.")
    menu = int(input("-> "))

    #
    # Opção 1
    #
    if (menu == 1):
        os.system('cls') # Limpa a tela do promt
        print("\n")
        print("+--------------------------------------------+")
        print("|       # CHAVES PÚBLICAS / PRIVADAS #       |")
        print("+--------------------------------------------+")
        print("\n\n")
        nipKey = input("Informe o nome do proprietario.\n-> ")

        print("Gerando número P")
        p = methods.gNumPrimo()
        print("Número P gerado. (P = " + str(p) + ")")

        print("Gerando número Q")
        q = methods.gNumPrimo()
        print("Número Q gerado. (Q = " + str(q) + ")")

        print("Gerando número N")
        n = p * q
        print("Número N gerado. (N = " + str(n) + ")")

        print("Calculando o Totient de P")
        phiP = methods.totient(p)
        print("Totient de P calculado. (PhiP = " + str(phiP) + ")")

        print("Calculando o Totient de Q")
        phiQ = methods.totient(q)
        print("Totient de Q calculado. (PhiQ = " + str(phiQ) + ")")

        print("Calculando o Totient de N")
        phiN = phiP * phiQ
        print("Totient de N calculado. (PhiN = " + str(phiN) + ")\n")

        print("Calculando o número E, dentro das condições [ 1 < E < Phi(N) ]")
        e = methods.numE(phiN)
        print("Número E calculado. (E = " + str(e) + ")\n\n")

        # Gerando arquivo da chave publica
        with open(("bin/publicKeys/" + nipKey + ".hsk"), "w") as file:
            # Chave Publica
            publicKey = [n, e]
            print("Sua chave pública é: (N = " + str(publicKey[0]) + ") e (E = " + str(publicKey[1]) + ")")
            print(publicKey[0], file=file)
            print(publicKey[1], file=file)
            file.close()

        # Gerando arquivo da chave privada
        with open(("bin/privateKeys/" + nipKey + ".phsk"), "w") as file:
            # Chave Privada
            privateKey = methods.gPrivateKey(phiN, e)
            print("Sua chave privada é: (N = " + str(n) + ") e (D = " + str(privateKey) + ")\n\n")
            print(n, file=file)
            print(privateKey, file=file)
            file.close()

        os.system('cls') # Limpa a tela do promt
        return main()

    #
    # Opção 2
    # Continuar edição aqui.......
    elif (menu == 2):
        os.system('cls') # Limpa a tela do promt
        print("\n")
        print("+--------------------------------------------+")
        print("|                 # CIFRA #                  |")
        print("+--------------------------------------------+")
        print("\n\n")

        fileName = input("Informe o nome do arquivo que deseja cifra.\n-> ")
        nipKey = input("Informe o nip da chave que deseja cifrar.\n-> ")

        methods.cifra(fileName, nipKey)

        return main()

    #
    # Opção 3
    #
    elif (menu == 3):
        os.system('cls') # Limpa a tela do promt
        print("\n")
        print("+--------------------------------------------+")
        print("|                # DECIFRA #                 |")
        print("+--------------------------------------------+")
        print("\n\n")

        fileName = input ( "Informe o nome do arquivo que deseja decifrar.\n-> " )
        nipKey = input ( "Informe o nip da chave PRIVADA.\n-> " )

        methods.descifra(fileName, nipKey)

        return main()

    #
    # Opção 0
    #
    elif (menu == 0):
        print("\n")
        print("+-------------------------------+")
        print("|      PROGRAMA ENCERRADO!      |")
        print("+-------------------------------+")
        quit()
    else:
        print("Informe um valor valido")
        return main()