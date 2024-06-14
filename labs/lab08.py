def main():
    linha,coluna = map(int, input().split(','))
    area = encontrar_area(linha)
    arvores_candidatas = parte_um(linha,coluna,area)
    dict_candidatas, arvore_escolhida = parte_dois(arvores_candidatas,area,linha,coluna)
    print('Árvores candidatas:')
    for items in arvores_candidatas:
        print(f'{items[0]},{items[1]}')
    print('Árvore escolhida:')
    print(f'{arvore_escolhida[0]},{arvore_escolhida[1]} com {dict_candidatas[arvore_escolhida]} árvores visíveis.')
    
def encontrar_area(linha): #Gera uma matriz cujas linhas são formadas pelo input do usuário
    area = []
    for _ in range(int(linha)):
        area.append([int(i) for i in input()]) #
    return area

def parte_um(linha,coluna,area): #Retorna a posição das arvores que não são visiveis do exterior da área analisada.
    arvores_candidatas =  [(i,j) for i in range(linha) for j in range(coluna) if any(area[i][k] >= area[i][j] for k in range(j)) and any(area[i][k] >= area[i][j] for k in range(j + 1,coluna)) and any(area[k][j] >= area[i][j] for k in range(i)) and any(area[k][j] >= area[i][j] for k in range(i + 1,linha))]
    return arvores_candidatas

def parte_dois(arvores_candidatas,area,linha,coluna):
    dict_candidatas = {i:0 for i in arvores_candidatas}
    for arvore in dict_candidatas.keys():
        x = arvore[0]
        y = arvore[1]
        h = area[x][y] #Armazena a altura da árvore candidata à observatório

        #Norte
        try:
            for a in range(1,max([linha,coluna])):
                if x - a < 0:
                    break
                elif area[x - a][y] >= h:
                    dict_candidatas[arvore] += 1
                    break
                elif h > area[x - a][y]:
                    dict_candidatas[arvore] += 1
        except IndexError: 
            pass

        #Sul
        try:
            for a in range(1,max([linha,coluna])):
                if area[x + a][y] >= h:
                    dict_candidatas[arvore] += 1
                    break
                elif h > area[x + a][y]:
                    dict_candidatas[arvore] += 1
        except IndexError: 
            pass


        #Oeste -- 
        try:
            for a in range(1,max([linha,coluna])):
                if h > area[x][y + a]:
                    dict_candidatas[arvore] += 1
                elif area[x][y + a] >= h:
                    dict_candidatas[arvore] += 1
                    break
        except IndexError: 
            pass

        #Leste --
        try:
            for a in range(1,max([linha,coluna])):
                if y - a < 0:
                    break
                elif area[x][y - a] >= h:
                    dict_candidatas[arvore] += 1
                    break
                elif h > area[x][y - a]:
                    dict_candidatas[arvore] += 1
        except IndexError: 
            pass

        #Nordeste --
        try:
            for a in range(1,max([linha,coluna])):
                if x - a < 0:
                    break
                elif area[x - a][y + a] >= h:
                    dict_candidatas[arvore] += 1
                    break
                elif h > area[x - a][y + a]:
                    dict_candidatas[arvore] += 1
        except IndexError: 
            pass

        #Noroeste --
        try:
            for a in range(1,max([linha,coluna])):
                if x-a < 0 or y - a < 0:
                    break
                if area[x - a][y - a] >= h:
                    dict_candidatas[arvore] += 1
                    break
                elif h > area[x - a][y - a]:
                    dict_candidatas[arvore] += 1
        except IndexError: 
            pass      

        #Sudeste --
        try:
            for a in range(1,max([linha,coluna])):
                if area[x + a][y + a] >= h:
                    dict_candidatas[arvore] += 1
                    break
                elif h > area[x + a][y + a]:
                    dict_candidatas[arvore] += 1
        except IndexError: 
            pass   

        #Sudoeste -- 
        try:
            for a in range(1,max([linha,coluna])):
                if y - a < 0:
                    break
                elif area[x + a][y - a] >= h:
                    dict_candidatas[arvore] += 1
                    break
                elif h > area[x + a][y - a]:
                    dict_candidatas[arvore] += 1
        except IndexError: 
            pass   
    
    #Seleciona, do dicionário, a árvore com maior valor
    arvore_escolhida = [arvore[0] for arvore in dict_candidatas.items() if max(dict_candidatas.values()) == arvore[1]]
    return dict_candidatas, arvore_escolhida[0]

if __name__ == "__main__":
    main()
    #Roda o código completo