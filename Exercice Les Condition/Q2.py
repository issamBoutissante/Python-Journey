#2. Écrivez un programme pour vérifier si un nombre est divisible par 3 et 13 ou non.
nombre=int(input("Entrer un nombre : "))
if nombre%3==0 and nombre%13==0:
    print("Le nombre est divisible par 3 et 13")
else:
    print("Le nombre n'est divisible par 3 et 13")