import math
import random
print("------------")
print("inistialisation")
print("les valeurs a virgule doivent etre inscrit de la sorte (3.6)")
print("------------")
v = float(input("Entrer   la premiere valeur --> "))
d = float(input("Ici la deuxieme si aucne valeur mettre 0 et + a la demande du signe --> "))
c = input("Ici veuillez inscrire le signe si aucune operation utliser + (valeur prise en compte +,-,/,*) --> ")
if c=="-":
 x= v-d
elif c=="+":
    x= v+d
elif c=="/":
    x= v/d
elif c=="*":
    x= v*d
print("Veuillez noter que c'est le resultat de l'operation ",x)
if x>=0:
    distance = x
    print("Voila la distance",distance)
else:
    distance = -x
    print(distance)

