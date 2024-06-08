mochila = input().split(' ') #Entrar com os itens e separá-los por mochila
compartimento = []
saidas = []

#Definição dos itens contidos por compartimento. A lista "compartimento" é formado por pares dos compartimentos da mochila i
for itens in mochila:
    divisor = round(len(itens)/2)
    compartimento.append(itens[0:divisor]) #Adição dos itens do primeiro compartimento da mochila i à lista "compartimentos"
    compartimento.append(itens[divisor:]) #Adiçao dos itens do segundo compartimento da mochila i à lista "compartimentos"
    
for i in range(0,len(compartimento),2): #iterar pela lista compartimento aos pares
    controle=0

    for elemento in compartimento[i]: #iterar pelos caracteres de uma string contando sua recorrência
        num1 = compartimento[i].count(elemento)
        num2 = compartimento[i+1].count(elemento)

        if num1 > 0 and num2 > 0: #comparação das strings
            saidas.append(elemento)
            break
        else:
            controle += 1

    if controle == len(compartimento[i]):
        saidas.append('Sem item repetido')

#print das saidas
for posição in range(0,len(saidas)):
    print(f'mochila {posição+1}: {saidas[posição]}')
        
    

    