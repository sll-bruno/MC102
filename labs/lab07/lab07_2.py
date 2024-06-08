output = []
def main():
    N = int(input()) #Recebe numeros de casos de teste

    for _ in range(N):
        fruits_dict = {}

        M = int(input()) #Recebe quantidade de itens diponíveis na feira
        for i in range(M):
            fruit,price = input().split() #Recebe cada item disponivel junto com o seu valor
            fruits_dict[fruit] = float(price)

        P = int(input()) #Recebe quantidade de itens que serão comprados
        sum = 0
        for j in range(P):
            fruit,num = input().split() #Recebe item que será comprado junto com a quantidade
            sum += (int(num) * fruits_dict[fruit])
        output.append(f'R$ {sum:.2f}')
    
if __name__ == "__main__":
    main()
    for itens in output:
        print(itens)