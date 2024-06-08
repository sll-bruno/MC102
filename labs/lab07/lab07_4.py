T = int(input())

for _ in range(T):
    M,N = map(int,input().split())
    dict_pt_jp = {} #Recebe, em um conjunto chave-valor, o texto em japones e sua tradução em portugues, respectivamente

    for i in range(M): #Recebe os textos e suas traduções
        text = input()
        translate = input()

        dict_pt_jp[text] = translate
    
    for j in range(N): #Recebe o texto a ser traduzido
        letra = input().split()

        for i in range(len(letra)):
            try:
                letra[i] = dict_pt_jp[letra[i]]
            except:
                pass
        print(*letra,sep=' ')
    print()

