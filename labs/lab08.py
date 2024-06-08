def main():
    linha,coluna = map(int, input().split(','))
    area = encontrar_area(linha)
    arvores_candidatas = parte_um(linha,coluna,area)
    print(arvores_candidatas)
    
def encontrar_area(linha): #Gera uma matriz cujas linhas são formadas pelo input do usuário
    area = []
    for _ in range(int(linha)):
        area.append([int(i) for i in input()]) #
    return area

def parte_um(linha,coluna,area): #Retorna a posição das arvores que não são visiveis do exterior da área analisada.
    arvores_candidatas =  [(i,j) for i in range(linha) for j in range(coluna) if any(area[i][k] >= area[i][j] for k in range(j)) and any(area[i][k] >= area[i][j] for k in range(j + 1,coluna)) and any(area[k][j] >= area[i][j] for k in range(i)) and any(area[k][j] >= area[i][j] for k in range(i + 1,linha))]
    return arvores_candidatas

if __name__ == "__main__":
    main()