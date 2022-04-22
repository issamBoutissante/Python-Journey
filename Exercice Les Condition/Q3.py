"""
3. Écrivez un programme pour vérifier si l'année donnée par l'utilisateur est
bissextile ou non. Année bissextile c'est une année spéciale contenant un jour
supplémentaire, soit un total de 366 jours dans une année. Une année est
considérée comme une année bissextile si l'année est exactement divisible par 4
mais non divisible par 100. L'année est également une année bissextile si elle est
exactement divisible par 400.
"""
annee=int(input("Donner une annee : "))
if annee%4==0 and annee%100!=0:
    print("L'annee est bissextile")
else:
    print("L'annee n'est pas bissextile")