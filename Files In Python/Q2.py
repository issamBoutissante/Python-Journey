#2.Écrivez un script qui compte le nombre de mots d’un fichier texte.
nombreMots=0
with open('text.txt','r') as file:
    for line in file.readlines():
        nombreMots+=len(line.split())
print(nombreMots)        