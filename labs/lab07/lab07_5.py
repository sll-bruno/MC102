while True:
    N,M = map(int, input().split())
    dict_servers = {}
    dict_clients = {}

    if M == 0 and N == 0:
        break

    for i in range(N): #Gera um dicionário contendo, para cada chave Qi, um valor correspondente às aplicações fornecidas
        Qi = input().split(' ')
        dict_servers[i] = Qi[1::]
        servers_ofert = list(dict_servers.values())

    for j in range(M): #Gera um dicionário contendo, para cada chave Pj, um valor correspondente às demandas do cliente
        Pj = input().split()
        dict_clients[j] = Pj[1::]
        client_demand = dict_clients.values()

    sum = 0
    for demand in client_demand:
        for ofert in servers_ofert:
            for i in demand:
                counter = ofert.count(i)
                sum += counter
                if counter != 0:
                    break
 
    print(sum)


        