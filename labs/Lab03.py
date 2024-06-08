X,Y=input().split(' ')
multiplo=1

for i in range(1,int(Y)+1):
    if i==(int(X)*multiplo):
        print(i)
        multiplo+=1
    else:
        print(i,end=' ')
           

    
