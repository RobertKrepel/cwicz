N=8
MAKS=20
a=[0]*N
for i in range(N):
    a[i]=int(input("Podaj liczbę od 0 do 20 "))
print(a)
liczniki=[0]*(MAKS+1)
for i in range(N):
    liczniki[a[i]]=liczniki[a[i]]+1
print (liczniki)
poz=0
for i in range(MAKS+1):
    for j in range(liczniki[i]):
        a[poz]=i
        poz=poz+1
print(a)
