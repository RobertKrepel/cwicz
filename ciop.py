wyraz1=[4,5,6,7]
wyraz2=wyraz1
wyraz1[0]=8
print(wyraz2)
print(id(wyraz1))
print(id(wyraz2))
print(wyraz2 is wyraz1)
