print ("Program liczy BMI")
waga=float(input("Podaj wagę w kilogramach "))
wzrost=float(input("Podaj wzrost w metrach "))
bmi=waga/wzrost**2
print ("Twoje BMI wynosi ",bmi)
if bmi<16:
    print ("wygłodzenie")
elif bmi<17:
    print ("wychudzenie")
elif bmi<18.5:
    print ("niedowaga")
elif bmi<25:
    print ("waga prawidłowa")
elif bmi<30:
    print ("nadwaga")
elif bmi<35:
    print ("otyłość")
else:
    print ("sumo")
    
             
