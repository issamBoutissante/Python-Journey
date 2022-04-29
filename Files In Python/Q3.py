# 3. Écrivez un script qui génère automatiquement un fichier texte contenant les tables de
# multiplication de 1 à 9 (chacune d’entre elles incluant 10 termes seulement).

with open("Multiplication.txt","w") as file:
    for i in range(1,10):
        file.write("\tMultiplication de "+str(i)+"\n")
        for j in range(1,10):
            file.write(str(i)+"*"+str(j)+"="+str(i*j)+"\n")
