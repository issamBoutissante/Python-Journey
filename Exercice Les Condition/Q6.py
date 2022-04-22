"""
Écrivez un programme pour vérifier si un alphabet est une voyelle ou une
consonne. Les lettres a, e, i, o et u en minuscules et en majuscules sont appelées
voyelles. Les alphabets autres que les voyelles sont appelés consonnes.
"""
alphabet=input("Entrer un alphabet : ")[0].lower()
voyelles=['a','e','i','o','u']
if alphabet in voyelles:
    print("Voyelle....")
else:    
    print("Consonne....")