from math import *
import time
print("------------")
time.sleep(0.3)
print("By Snipeur060")
time.sleep(0.3)
print("Théorème de Pythagore")
time.sleep(0.3)
print("Ici il nous manque l'hypothénuse ")
time.sleep(0.3)
print("Attention à l'unité")
time.sleep(0.3)
print("------------")
fir = float(input("Ici la longueur de votre premier côté--> "))
sec = float(input("Ici la longueur de votre deuxième côté--> "))
op = int(input("Mettre 1 pour la méthode détaillé et 2 pour le resultat directement--> "))
if op == 1:
 tir = fir**2
 print("Nous elevons au carré la première valeur ici",fir, " donc", fir, "²"," Le resultat sera", tir)
 tir2 = sec**2
 print("Nous elevons au carré la deuxième valeur ici",sec, " donc", sec, "²"," Le resultat sera", tir2)
 print("Nous allons additionner les deux carrés")
 rac = tir + tir2
 print("Donc ",tir,"+",tir2," qui fait", rac)
 print("Ici je vais faire la racine carré de cette addition")
 res = sqrt(rac)
 print("Le résultat est alors de ", res)
 print("Ou alors racine carré de", rac)
 
else :
   res = sqrt(fir**2+sec**2)
   print("L'hypothénuse fait ", res)
