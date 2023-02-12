def enum_weights(tab):
    i = 0
    while i<10 :
        i += 1
        x = input("Weight number " + str(i) + " : ")
        if x == "stop":
            if len(tab) == 0:
                print("Impossible")
                sys.exit()
            else:
                break
        elif type(x) is int or float:
            tab.append(x)
            print(tab)
            continue
        else:
            print("You can only enter integers or decimal numbers, or wri    te stop when all values have been entered.\n")
            continue

def calcul_weights(p, tab):
    tab_size = len(tab)
    i = 0
    p = p / 2
    print("You must therefore add this weight on each side of the bar : " + str(p))
    nombre_de_poids = []
    while i < tab_size:
        nombre_de_poids.append(float(p) // float(tab[i]))
        p = float(p) % float(tab[i])
        i += 1
    i -= tab_size
    while i < tab_size:
        print("You need to add " + str(nombre_de_poids[i]) + " weight of " + str(tab[i]))
        i += 1

