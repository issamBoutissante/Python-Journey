# Écrivez un script qui recopie une chaîne dans une nouvelle variable, en insérant
# des astérisques entre les caractères. Ainsi par exemple, « gaston » devra devenir
# « g*a*s*t*o*n »
chaine=input("Entrer une chaine : ")
newChaine=""
for char in chaine:
    newChaine+=char+"*"
        