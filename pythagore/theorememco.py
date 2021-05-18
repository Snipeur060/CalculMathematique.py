from math import *
import time
print("------------")
time.sleep(0.3)
print("By Snipeur060")
time.sleep(0.3)
print("Theoreme de Pythagore")
time.sleep(0.3)
print("Ici il nous manque un cote mais nous avons l'hypothenuse")
time.sleep(0.3)
print("Attention à l'unite")
time.sleep(0.3)
print("------------")
fir = float(input("Ici la longueur de votre premier cote--> "))
sec = float(input("Ici la longueur de votre hypoténuse cote--> "))
op = int(input("Mettre 1 pour la methode detaille et 2 pour le resultat directement--> "))
if op == 1:
 tir = fir**2
 print("Nous elevons au carre la premiere valeur ici",fir, " donc", fir, "²"," Le resultat sera", tir)
 tir2 = sec**2
 print("Nous elevons au carre la deuxieme valeur ici",sec, " donc", sec, "²"," Le resultat sera", tir2)
 print("Nous allons soustraire les deux carres")
 rac = tir2 - tir
 print("Donc ",tir2,"-",tir," qui fait", rac)
 print("Ici je vais faire la racine carre de cette soustraction")
 res = sqrt(rac)
 print("Le resultat est alors de ", res)
 print("Ou alors racine carre de", rac)
 
else :
   res = sqrt(sec**2-fir**2)
   print("Le cote fait ", res)
