#Écrivez un programme qui vérifie si un nombre donné est premier ou non
nombre=int(input("Entrer un nombre : "))
isPremier=True
din=nombre-1
while din>1:
    if nombre%din==0:
        isPremier=False
        break
    din-=1
if isPremier:
    print("Premier")
else:
    print("N'est pas Premier")