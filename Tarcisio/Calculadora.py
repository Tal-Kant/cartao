#Calculadora Básica....

#importando a classe os
import os

#Interface com o usuário:
while (True):
    #Menu
    print('Menu:')
  
    print('\n1 - Somar')
    print("2 - Subtrair ")
    print("3 - Multiplicar ")
    print("4 - Dividir ")
    
    
    op = int(input("\nEscolha sua opção! (Digite '0' para sair)"))
    
    #Módulos de Cálculos
    if op == 1:
        pass
    elif op == 2:
        pass
    elif op == 3:
        pass
    elif op == 4:
        os.system("cls")
        print("Módulo de Divisão...\n")
        continuar = True
        while continuar is True:
            v1 = float(input("Digite um valor: "))
            v2 = float(input("Digite outro valor: "))
            if v2 != 0:
                print("\n O valor da divisão é: {:.2f}".format(v1 / v2))
            else:
                print("Impossível dividir por ZERO!!!!")
                
            continuar = int(input("\n Deseja continuar dividindo? (1-Sim/2-Não): "))
            
            if continuar == 1:
                continuar = True
                os.system("clear")
            elif continuar == 2:
                os.system("clear")
                
    elif op < 0 or op > 4:
        print("\n Opção Inválida! Tente Novamente.....")