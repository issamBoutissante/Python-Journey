#Écrire un programme qui affiche la table de multiplication d’un nombre donné
nombre=int(input("Entrer un nombre : "))
i=0
while i<=9:
    print(nombre,"*",i,"=",nombre*i)
    i+=1