from func import *

poids = []

print("Value of available weights from heaviest to lightest :\n Type \"stop\" when you're done.\n")

enum_weights(poids) #entrer la valeur des poids disponibles

p_barre = input("The weight of the bar : ") #poids de la barre
p_total = input("Whats's the total weight you want to lift ?\n") #poids total à soulever
p_sou = float(p_total) - float(p_barre) #poids à soulever sans la barre

calcul_weights(p_sou, poids)

print("on each side of the bar if you want to lift " + str(p_total))
