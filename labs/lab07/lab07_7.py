N = int(input())

for _ in range(N):
    lista_repetida = input().split()
    lista_sem_repeticao = list(set(lista_repetida))
    print(*sorted(lista_sem_repeticao))
