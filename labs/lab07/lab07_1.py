def main():
    N = int(input()) #Recebe o numero de casos de teste
    espaço_vazio = input()

    for j in range(N):
        dict_arvores = {}
        contador = 0
        i = True
        while i == True: #Inicia um loop infinito que recebe as espécies de arvores presentes no caso de teste, armazenando suas quantidades em um dicionário
            try:
                especie = input()
            except:
                break
            
            if not especie: #Verifica se a varíavel especie esta vazia; em caso True, passa para o próximo caso de teste
                i = False
            elif especie in dict_arvores:
                dict_arvores[especie] += 1
                contador += 1
            elif especie not in dict_arvores:
                dict_arvores[especie] = 1
                contador += 1
            
        for keys in sorted(dict_arvores.keys()): #Printa a porcentagem de cada espécie de árvore em ordem alfabética
            print((f'{keys} {(dict_arvores[keys]/contador)*100:.4f}'))

        if j == N - 1:
            break
        else:
            print()
    
if __name__ == '__main__':
    main()
