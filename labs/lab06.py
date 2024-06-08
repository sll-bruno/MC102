lista = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

keys_dict = {}
def is_valid_key(key): #Checks if the user input is a valid key
    valid_characters = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    for letter in str(key):
        if letter not in valid_characters or len(key) != 5:
            return False
        else:
            continue

    #Stores the value of the key in a dictionary
    if user_input == 'public_key':
        keys_dict[user_input] = [lista.index(i) for i in key]
    else:
        keys_dict[user_input] = [lista.index(i) for i in key]
    return True, keys_dict 

def is_inverse(keys_dict):
    '''
    Função que verífica se o shift publico e privados são inveros um do outro. 
    '''
    if keys_dict['public_key'] == keys_dict['private_key'][::-1]:
        return True
    else: 
        return False

def find_shifts(keys_dict):
    '''Essa função retorna o uma lista de shifts que devem ser apkicados na criptografia e na descriptografia'''
    public_key = keys_dict['public_key']
    private_key = keys_dict['private_key']
    shifts = [private_key[i] - public_key[i]  for i in range(5)]
    for i in range(len(shifts)):
        if shifts[i] > 26:
            shifts[i] -= 62
        elif shifts[i] < - 26:
            shifts[i] += 62

    return shifts

def shift_encrypt(message, shifts):
    '''Retorna o valor criptografado da mensagem para um shift fixo'''
    encrypted_message = []

    global lista
    for caracter in message: 
        try:
            encrypted_character = lista[lista.index(caracter) + shifts[0]]
        except IndexError:
            if lista.index(caracter) + shifts[0] < 0:
                encrypted_character = lista[62 - shifts[0] +1 + lista.index(caracter)]
            else:
                encrypted_character = lista[abs(shifts[0]) - (len(lista) - lista.index(caracter))]
        encrypted_message.append(encrypted_character)

    encrypted_message = ''.join(encrypted_message) #Transforma a mensagem de indices para os carácteres correspondentes
    return encrypted_message

def alternated_shifts_encrypt(message, shifts): 
    '''Criptografa a mensagem recebida utilizando so shift alternado'''
    encrypted_message = []
    
    for i in range(len(message)):
            if i % 2 == 0:
                try:
                    encrypted_character = lista[lista.index(message[i]) + shifts[0]]
                except IndexError:
                    encrypted_character = lista[shifts[0] - (len(lista) - lista.index(message[i]))]
            else:
                try:
                    encrypted_character = lista[lista.index(message[i]) + shifts[1]]
                except IndexError:
                        encrypted_character = lista[abs(shifts[1]) - (len(lista) - lista.index(message[i]))]
            encrypted_message.append(encrypted_character)

    encrypted_message = ''.join(encrypted_message)
    return encrypted_message

def variable_shifts_encrypt(message, shifts): 
    '''Criptografa a mensagem recebida utilizando o shift variável'''
    encrypted_message = []

    for i in range(len(message)): #Criptografia dos caracteres da mensagem
            if i % 5 == 0:
                try:
                    character = lista[lista.index(message[i]) + shifts[0]]
                except IndexError:
                    character = lista[abs(shifts[0]) - 1 - (len(lista) - 1 - lista.index(message[i]))]
            elif i % 5 == 1:
                try:
                    character = lista[lista.index(message[i]) + shifts[1]]
                except IndexError:
                    character = lista[abs(shifts[1]) - 1 - (len(lista) - 1 - lista.index(message[i]))]
            elif i % 5 == 2:
                try:
                    character = lista[lista.index(message[i]) + shifts[2]]
                except IndexError:
                    character = lista[abs(shifts[2]) - 1 - (len(lista) -1 - lista.index(message[i]))]
            elif i % 5 == 3:
                try:
                    character = lista[lista.index(message[i]) + shifts[3]]
                except IndexError:
                    character = lista[abs(shifts[3]) - 1 - (len(lista) -1 - lista.index(message[i]))]
            else:
                try:
                    character = lista[lista.index(message[i]) + shifts[4]]
                except IndexError:
                        character = lista[abs(shifts[4]) - 1 - (len(lista) - 1 - lista.index(message[i]))]
            encrypted_message.append(character)

    encrypted_message = ''.join(encrypted_message)
    return encrypted_message

def shift_decrypt(encrypted_message,shifts):
    '''Descriptografa uma mensagem utilizando shift fixo'''
    decrypted_message = []

    global lista
    for caracter in encrypted_message: 
        try:
            decrypted_character = lista[lista.index(caracter) - shifts[0]]
        except IndexError:
            if lista.index(caracter) - shifts[0] < 0:
                decrypted_character = lista[62 - shifts[0] + (lista.index(caracter))]
            else:
                decrypted_character = lista[abs(shifts[0]) - 1 - (len(lista) - 1 - lista.index(caracter))]
        decrypted_message.append(decrypted_character)

    decrypted_message = ''.join(decrypted_message) 
    return decrypted_message

def alternated_shifts_decrypt(message, shifts):
    '''Descriptografa uma mensagem utilizando o shift alternado'''
    decrypted_message = []
    
    for caracter in message:
            if message.index(caracter) % 2 == 0:
                try:
                    encrypted_character = lista[lista.index(caracter) - shifts[0]]
                except IndexError:
                    encrypted_character =lista[abs(shifts[0]) - 1 - (len(lista) - 1 - lista.index(caracter))]
            else:
                try:
                    encrypted_character = lista[lista.index(caracter) - shifts[1]]
                except IndexError:
                    encrypted_character = lista[62 - shifts[1] + 1]
            decrypted_message.append(encrypted_character)

    decrypted_message = ''.join(decrypted_message)
    return decrypted_message

def variable_shifts_decrypt(message, shifts):
    '''Descriptografa uma mensagem utilizando shift variável'''
    decrypted_message = []

    for i in range(len(message)): #Criptografia dos caracteres da mensagem      
            if i % 5 == 0:
                try:
                    decrypted_character = lista[lista.index(message[i]) - shifts[0]]
                except IndexError:
                    decrypted_character = lista[abs(shifts[0]) - 1]

            elif i % 5 == 1:
                try:
                    decrypted_character = lista[lista.index(message[i]) - shifts[1]]
                except IndexError:
                    decrypted_character = lista[abs(shifts[1]) - 1]

            elif i % 5 == 2:
                try:
                    decrypted_character = lista[lista.index(message[i]) - shifts[2]]
                except IndexError:
                    decrypted_character = lista[abs(shifts[2]) - 1]

            elif i % 5 == 3:
                try:
                    decrypted_character = lista[lista.index(message[i]) - shifts[3]]
                except IndexError:
                    decrypted_character = lista[abs(shifts[3]) - 1]

            else:
                try:
                    decrypted_character = lista[lista.index(message[i]) - shifts[4]]
                except IndexError:
                    decrypted_character = lista[abs(shifts[4]) - 1]
            decrypted_message.append(decrypted_character)

    decrypted_message = ''.join(decrypted_message)
    return decrypted_message

while True: #Aguarda a entrada do usúario em um loop infinito
    user_input = input()
    
#match user_input: 
    if user_input == 'public_key' or user_input == 'private_key':
        key = input()
        if is_valid_key(key): #If the key is valid
            if user_input == 'public_key':
                print('Chave pública válida')
            else:
                print('Chave privada válida')
        else: # If the key is not valid
            if user_input =='public_key':
                print('Chave pública inválida')
            else:
                print('Chave privada inválida')

    elif user_input == 'encrypt':
        message = input()
        shifts = find_shifts(keys_dict)
        if is_inverse(keys_dict): #Função inverse: Inverts and prints the string message
            print(f'Mensagem criptografada:{message[::-1]}')
        elif len(set(shifts)) == 1: #Se todos os elementos da lista são iguais, ísto é, se o conjunto formado por essa lista tiver apenas um elemento: Shift fixo
            encrypted_message = shift_encrypt(message,shifts)
            print(f'Mensagem criptografada:{encrypted_message}')
        elif len(set(shifts)) == 2:
            encrypted_message = alternated_shifts_encrypt(message, shifts) #Se existem apenas dois elementos diferentes entre si no shift, isto é, se o conjunto formado por essa lista tiver dois elementos: Shift alternado
            print(f'Mensagem criptografada:{encrypted_message}')
        else:
            encrypted_message = variable_shifts_encrypt(message, shifts)
            print(f'Mensagem criptografada:{encrypted_message}')

    elif user_input == 'decrypt':
        encrypted_message = input()
        shifts = find_shifts(keys_dict)
        if is_inverse(keys_dict):
            print(f'Mensagem descriptografada:{encrypted_message[::-1]}')
        elif len(set(shifts)) == 1: #Se todos os elementos da lista são iguais, ísto é, se o conjunto formado por essa lista tiver apenas um elemento: Shift fixo
            decrypted_message = shift_decrypt(encrypted_message,shifts)
            print(f'Mensagem descriptografada:{decrypted_message}')
        elif len(set(shifts)) == 2: #Se existem apenas dois elementos diferentes entre si no shift, isto é, se o conjunto formado por essa lista tiver dois elementos: Shift alternado
            decrypted_message = alternated_shifts_decrypt(encrypted_message, shifts)
            print(f'Mensagem descriptografada:{decrypted_message}')
        else:
                decrypted_message = variable_shifts_decrypt(encrypted_message, shifts)
                print(f'Mensagem descriptograda:{decrypted_message}')
    elif user_input == 'Exit': #O código é interrompido se "Exit" for digitado
        break
