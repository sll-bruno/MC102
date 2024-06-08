notas_dict = {'W': 1, 'H': 0.5, 'Q': 0.25, 'E': 0.125, 'S': 0.0625, 'T': 0.03125, 'X': 0.015625} #Armazena, em um dicionário, as notas como chaves e os tempos como respectivos valores
output = []

while True: #Aguarda a entrada dos casos de teste em um loop infinito
    user_input = input()
    counter = 0 #Conta quantos compassos tem o tempo correto

    if user_input == '*':
        break
    else:
        user_input = user_input[1:-1].split('/')

        for compassos in user_input:
            sum = 0
            for nota in compassos:
                sum += notas_dict[nota]

            if sum == 1:
                counter += 1
            else:
                continue
    output.append(counter)

for itens in output:
        print(itens)

