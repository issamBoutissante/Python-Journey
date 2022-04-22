#Écrivez un programme pour entrer le numéro du mois entre (1-12) et afficher le
#nombre de jours de ce mois.
mois=int(input("Entrer un mois : "))
if mois==2:
    print("28 jours ...")
elif mois%2==0:
    print("30 jours ...")
else:
    print("31 jours ...")