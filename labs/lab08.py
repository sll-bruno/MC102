def main():
    linha,coluna = map(int, input().split(','))
    area = encontrar_area(linha)
    arvores_candidatas = parte_um(linha,coluna,area)
    dict_candidatas, arvore_escolhida = parte_dois(arvores_candidatas,area)
    print('Arvores candidatas:')
    print(*arvores_candidatas,sep='\n')
    print('Árvore escolhida:')
    print(f'{arvore_escolhida} com {dict_candidatas[arvore_escolhida]} árvores visíveis')
    
def encontrar_area(linha): #Gera uma matriz cujas linhas são formadas pelo input do usuário
    area = []
    for _ in range(int(linha)):
        area.append([int(i) for i in input()]) #
    return area

def parte_um(linha,coluna,area): #Retorna a posição das arvores que não são visiveis do exterior da área analisada.
    arvores_candidatas =  [(i,j) for i in range(linha) for j in range(coluna) if any(area[i][k] >= area[i][j] for k in range(j)) and any(area[i][k] >= area[i][j] for k in range(j + 1,coluna)) and any(area[k][j] >= area[i][j] for k in range(i)) and any(area[k][j] >= area[i][j] for k in range(i + 1,linha))]
    return arvores_candidatas

def parte_dois(arvores_candidatas,area):
    dict_candidatas = {i:0 for i in arvores_candidatas}
    for arvore in dict_candidatas.keys():
        x = arvore[0]
        y = arvore[1]
        h = area[x][y]
        a = 1

        #Norte
        try:
            while h < area[x - a][y]:
                dict_candidatas[arvore] += 1
                a += 1
                if area[x-a][y] >= h:
                    dict_candidatas[arvore] += 1
                    break
        except IndexError:
            pass
        finally:
            dict_candidatas[arvore] += 1

        #Sul
        try:
            while h < area[x + a][y]:
                dict_candidatas[arvore] += 1
                a += 1
                if area[x-a][y] >= h:
                    dict_candidatas[arvore] += 1
                    break
        except IndexError:
            pass
        finally:
            dict_candidatas[arvore] += 1   


        #Oeste
        try:
            while h < area[x][y + a]:
                dict_candidatas[arvore] += 1
                a += 1
                if area[x-a][y] >= h:
                    dict_candidatas[arvore] += 1
                    break
        except IndexError:
            pass
        finally:
            dict_candidatas[arvore] += 1

        #Leste
        try:
            while h < area[x][y - a]:
                dict_candidatas[arvore] += 1
                a += 1
                if area[x-a][y] >= h:
                    dict_candidatas[arvore] += 1
                    break
        except IndexError:
            pass
        finally:
            dict_candidatas[arvore] += 1

        #Nordeste
        try:
            while h < area[x - a][y + a]:
                dict_candidatas[arvore] += 1
                a += 1
                if area[x-a][y] >= h:
                    dict_candidatas[arvore] += 1
                    break
        except IndexError:
            pass
        finally:
            dict_candidatas[arvore] += 1

        #Noroeste
        try:
            while h < area[x - a][y - a]:
                dict_candidatas[arvore] += 1
                a += 1
                if area[x-a][y] >= h:
                    dict_candidatas[arvore] += 1
                    break
        except IndexError:
            pass
        finally:
            dict_candidatas[arvore] += 1        

        #Sudeste
        try:
            while h < area[x + a][y + a]:
                dict_candidatas[arvore] += 1
                a += 1
                if area[x-a][y] >= h:
                    dict_candidatas[arvore] += 1
                    break
        except IndexError:
            pass
        finally:
            dict_candidatas[arvore] += 1

        #Sudoeste
        try:
            while h < area[x + a][y - a]:
                dict_candidatas[arvore] += 1
                a += 1
                if area[x-a][y] >= h:
                    dict_candidatas[arvore] += 1
                    break
        except IndexError:
            pass
        finally:
            dict_candidatas[arvore] += 1
    
    #Seleciona, do dicionário, a árvore com maior valor
    arvore_escolhida = [arvore[0] for arvore in dict_candidatas.items() if max(dict_candidatas.values()) == arvore[1]]
    return dict_candidatas, arvore_escolhida[0]

if __name__ == "__main__":
    main()
    #Roda o código completo