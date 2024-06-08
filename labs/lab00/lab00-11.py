x=float(input())
cem=x//100
cinquenta=(x%100)//50
vinte=(x%100%50)//20
dez=(x%100%50%20)//10
cinco=(x%100%50%20%10)//5
dois=(x%100%50%20%10%5)//2
um=(x%100%50%20%10%5%2)//1
print('NOTAS:')
print(int(cem),'nota(s) de R$ 100.00')
print(int(cinquenta),'nota(s) de R$ 50.00')
print(int(vinte),'nota(s) de R$ 20.00')
print(int(dez),'nota(s) de R$ 10.00')
print(int(cinco),'nota(s) de R$ 5.00')
print(int(dois),'nota(s) de R$ 2.00')

m050=x%100%50%20%10%5%2%1//0.50
m025=x%100%50%20%10%5%2%1%0.50//0.25
m010=x%100%50%20%10%5%2%1%0.50%0.25//0.10
m005=x%100%50%20%10%5%2%1%0.50%0.25%0.10//0.05
m001=x%100%50%20%10%5%2%1%0.50%0.25%0.10%0.05//0.01
print('MOEDAS:')
print(int(um),' moeda(s) de R$ 1.00\n',int(m050),' moeda(s) de R$ 0.50\n',int(m025),' moeda(s) de R$ 0.25\n',int(m010),' moeda(s) de R$ 0.10\n',int(m005),' moeda(s) de R$ 0.05\n', int(m001),' moeda(s) de R$ 0.01',sep='')

