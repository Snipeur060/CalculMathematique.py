from math import *
import time
print("------------")
time.sleep(0.3)
print("By Snipeur060")
time.sleep(0.3)
print("Théorème de Pythagore")
time.sleep(0.3)
print("Ici il nous manque un côté mais nous avons l'hypothénuse")
time.sleep(0.3)
print("Attention à l'unité")
time.sleep(0.3)
print("------------")
fir = float(input("Ici la longueur de votre premier côté--> "))
sec = float(input("Ici la longueur de votre hypoténuse côté--> "))
op = int(input("Mettre 1 pour la méthode détaillé et 2 pour le resultat directement--> "))
if op == 1:
 tir = fir**2
 print("Nous elevons au carré la première valeur ici",fir, " donc", fir, "²"," Le resultat sera", tir)
 tir2 = sec**2
 print("Nous elevons au carré la deuxième valeur ici",sec, " donc", sec, "²"," Le resultat sera", tir2)
 print("Nous allons soustraire les deux carrés")
 rac = tir2 - tir
 print("Donc ",tir2,"-",tir," qui fait", rac)
 print("Ici je vais faire la racine carré de cette soustraction")
 res = sqrt(rac)
 print("Le résultat est alors de ", res)
 print("Ou alors racine carré de", rac)
 
else :
   res = sqrt(sec**2-fir**2)
   print("Le côté fait ", res)
