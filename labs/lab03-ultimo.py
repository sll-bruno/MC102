#Recebe como entrada o numero de casos de teste
T=int(input())
periodo=[]

#Recebe as populaçoes de A e B e seus respectivos crescimentos, calculando as populaçoes futuras a cada ano
for _ in range(T):
    PA,PB,G1,G2=input().split(' ')

    for anos in range(1,102):
        pop_futura_a=int(PA) +(int((float(G1)/100)*int(PA)))
        pop_futura_b=int(PB)+(int((float(G2)/100)*int(PB)))
        PA=pop_futura_a
        PB=pop_futura_b

        if anos>100:
            periodo.append('Mais de 1 seculo')
            break
        elif pop_futura_a>pop_futura_b:
            periodo.append(str(anos)+" anos")
            break

for i in periodo:
    print(i)
