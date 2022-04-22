# #1 
# prenom=input("entrer votre prenom ")
# age=input("entrer votre age ")
# print("Bonjour ",prenom,",vous etes ",age," ans.")

# #2 
# langeur=input("entrer la langeur ")
# print("la surface est ",float(langeur)**2)

# #3
# rayon = input("entrer le rayon ")
# print("le perimetre est ",(2*3.14*float(rayon)))

#4 
# print("entrer les information suivant :")
# nom=input("Nom : ")
# prenom=input("Prenom : ")
# age=input("Age : ")
# salaire=input("Salaire : ")
# prime=input("Prime : ")
# print(prenom,nom,"a",(int(age)+1),"ans")
# print(prenom,nom,"gagne Salaire total ",(float(salaire)+float(prime)*1.9))

#5
# seconds=int(input("entrer nombre de seconds : "))
# print(int(seconds/60/60)%24,":",int(seconds/60)%60,":",seconds%60)


# un salarie travail en mode vacataire 
# ecrire un programe qui calcule le salaire hebdomadaire et monsuelle de ce salaraie 
# en prenant en consederation que 17% de son salaire brut est alloue au retenue

nbHeurs=int(input("Donner le nombre d'heurs de travail par semmaine : "))
salaire=float(input("entrer votre salaire : "))
hebdomadaire=nbHeurs*salaire*0.83
print("Le salaire hebdomadaire est : ",hebdomadaire)
print("Le salaire mensuelle est : ",hebdomadaire*4)