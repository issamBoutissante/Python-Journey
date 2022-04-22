#Écrivez un programme qui demande deux nombres de l'utilisateur et trouve le
#plus grand diviseur commun
n1=int(input("Entrer Le Premier Nombre :"))
n2=int(input("Entrer Le Deuxieme Nombre :"))
diviseur=1
if n1<=n2:
    diviseur=n1
else:
    diviseur=n2

while diviseur>=1:
    if n1%diviseur==0 and n2%diviseur==0:
        print("La plus grand diviseur est : ",diviseur)    
        break