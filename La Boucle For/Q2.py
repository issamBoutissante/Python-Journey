#. Écrivez un script qui compte le nombre d'occurrences du caractère «e» dans une
#  chaîne.
chaine=input("Entrer une chaine : ")
i=0
for char in chaine:
    if char=='e':
        i+=1
print("Le nombre de 'e' son't :",i)        