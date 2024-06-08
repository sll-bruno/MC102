while True:
    dict_assinaturas = {}
    counter = 0

    N = int(input())

    if N == 0:
        break

    for _ in range(N):
        nome, assinatura_og = input().split()
        dict_assinaturas[nome] = assinatura_og

    M = int(input())

    for _ in range(M):
        nome, assinatura_aula = input().split()
        letras_erradas = 0
        
        for i in range(len(assinatura_aula)):

            if assinatura_aula[i] != dict_assinaturas[nome][i]:
                letras_erradas += 1
        if letras_erradas > 1:
            counter += 1
        
    print(counter)