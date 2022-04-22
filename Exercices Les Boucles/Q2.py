#Écrivez un programme qui demande un nombre et calcule sa factorielle.
nombre=int(input("Entrer un nombre : "))
factorielle=1
while nombre>1:
    factorielle=factorielle*nombre
    nombre=nombre-1 
print("Le Factorielle est : ",factorielle)