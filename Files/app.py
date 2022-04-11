myFile =open(r"C:\Users\ISSAM\Desktop\EMSI\3IIR S2\PFA\Python\Python Journey\Files\myFile.txt")
lines=myFile.readlines()
for line in lines:
    print(line.strip())
myFile.close()