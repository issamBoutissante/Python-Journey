#. Écrivez un programme pour saisir un caractère de l'utilisateur et vérifiez si le
# caractère donné est un alphabet, un chiffre ou un caractère spécial
char=input("Entrer un caractere special : ")
if ord(char[0])>=65 and ord(char[0])<=122:
    print("Lettre")
else:
    print("Not Lettre")