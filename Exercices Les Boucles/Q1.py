#Écrivez un programme pour trouver la somme de tous les entiers entre 1 et n
n=int(input("Entrer Un Nombre : "))
somme=0
i=1
while i<=n:
    somme+=i
    i=i+1
print("Somme est : ",somme)   