#1.Écrivez un script qui lit un fichier texte et affiche son contenu ligne par ligne.
with open('text.txt','r') as file:
    for line in file.readlines():
        print(line,end="")
