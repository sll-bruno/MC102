N = int(input())  #Recebendo a entrada dos alimentos e suas respectivas quantidades de nutrientes
saidas = []

tabela_nutricional = []
for i in range(N):  #Adicionando os parâmetros de cada alimento à tabela nutricional
    alimento = input().split(' ')  #Espera 4 entradas (Nome do alimento,ProteinPackets,CodeCarbs e DataLipids), parâmetros que caracterizam o alimento 
    alimento[1]=float(alimento[1])
    alimento[2]=float(alimento[2])
    alimento[3]=float(alimento[3])
    tabela_nutricional.extend([alimento])

M = int(input())
for _ in range(M):
    entrada=input().split() #Recebe o nome e a necessidade nutricional dos atletas
    nome_atleta=entrada[0]
    proteina_diario=float(entrada[1])
    carbo_diario=float(entrada[2])
    lipideo_diario=float(entrada[3])

    alimentacao=[] #Armazena os alimentos consumidos pelo atleta durante o dia
    for _ in range(3):
        refeição = input().split() #Recebe os alimentos consumidos no café da manha, almoço e janta.
        alimentacao.extend(refeição)
    
    saidas.append(nome_atleta)
    proteina_consumido = 0
    carbo_consumido = 0
    lipideo_consumido = 0

    for consumo in alimentacao: #Itera pela lista de alimentos consumidos durante o dia, comparando-os com os seus valores nutricionais em "tabela_nutricional" e os somando 
        for elemento in tabela_nutricional:
            if elemento[0] == consumo:
                proteina_consumido += float(elemento[1])
                carbo_consumido += float(elemento[2])
                lipideo_consumido += float(elemento[3])
                break
#Verifica se o consumo dos nutrientes superou, igualou ou ficou abaixo das necessidades diárias.
    if proteina_consumido - proteina_diario > 0:
        saidas.append(f"{abs(proteina_consumido - proteina_diario):.1f} gramas de ProteinPackets em excesso")
    elif proteina_consumido - proteina_diario < 0:
        saidas.append(f"{abs(proteina_consumido - proteina_diario):.1f} gramas de ProteinPackets em falta")
    else:
        saidas.append(f"{proteina_diario:.1f} gramas de ProteinPackets adequado")

    if carbo_consumido - carbo_diario > 0:
        saidas.append(f"{abs(carbo_consumido - carbo_diario):.1f} gramas de CodeCarbs em excesso")
    elif carbo_consumido - carbo_diario < 0:
        saidas.append(f"{abs(carbo_consumido - carbo_diario):.1f} gramas de CodeCarbs em falta")
    else:
        saidas.append(f"{carbo_diario:.1f} gramas de CodeCarbs adequado")

    if lipideo_consumido - lipideo_diario > 0:
        saidas.append(f"{abs(lipideo_consumido - lipideo_diario):.1f} gramas de DataLipids em excesso")
    elif lipideo_consumido - lipideo_diario < 0:
        saidas.append(f"{abs(lipideo_consumido - lipideo_diario):.1f} gramas de DataLipids em falta")
    else:
        saidas.append(f"{lipideo_diario:.1f} gramas de DataLipids adequado")

for i in saidas: #Printa o balanço nutricional dos atletas
    print(i)