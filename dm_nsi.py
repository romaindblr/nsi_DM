def init():
    print("Bonjour !!")
    print("Bienvenue sur mon programme de Conversion")
    print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
    print("1 : décimal")
    print("2 : binaire")
    print("3 : hexadécimal")
    print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
    choix = int(input("Quelle est ton unité de départ ? "))
    number = input("Quel est ton chiffre ? ")
    print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
    if choix == 1:
        print("binaire --> ", deci_to_bin(number))
        print("hexadécimal --> ", bin_to_hex(deci_to_bin(number)))
    elif choix == 2:
        print("décimal --> ", bin_to_deci(number))
        print("hexadécimal --> ", bin_to_hex(number))
    elif choix == 3:
        print("décimal --> ", hex_to_deci(number))
        print("binaire --> ", deci_to_bin(hex_to_deci(number)))
    else:
        print("Erreur dans le choix !")
        print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
        print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
        init()

def bin_to_deci(number):
    # initalisation de la liste
    number = str(number)
    liste = list(number)
    # conversion
    place = 0
    max = len(liste)-1
    conversion = 0
    while len(liste) != place:
        if int(liste[place]) == 1:
            mult = 2**max
            conversion = mult + conversion
            max -= 1
            place += 1
        else:
            max -= 1
            place += 1
    return conversion

def deci_to_bin(number):
    # initialisation de la liste
    number = int(number)
    liste = []
    # je convertis comme on convertit sur une feuille donc avec les puissances sur le chiffre 2
    puissance = 1
    while number >= 2 ** puissance:
        puissance += 1
    puissance -= 1
    while number != 0:
        if number >= 2**puissance:
            number = number - 2**puissance
            liste.append(1)
            puissance -= 1
            if number == 0:
                while puissance >= 0:
                    liste.append(0)
                    puissance -= 1
        elif number < 2**puissance:
            liste.append(0)
            puissance -= 1
    # conversion de la liste en chaine de caractères
    Liste = ''.join(str(elem) for elem in liste)
    return Liste

def bin_to_hex(number):
    # initialisation de la liste
    number = str(number)
    liste = list(number)
    liste = list(map(int, liste))
    # ajout de 0 pour avoir un multiple de 4
    while len(liste)%4 != 0:
        liste.insert(0, 0)
    # division en groupes de 4 bits
    debut = 0
    fin = 4
    liste_conversion = []
    while fin <= len(liste):
        liste_liste = liste[debut:fin]
        liste_conversion.append(liste_liste)
        debut += 4
        fin += 4
    # conversion de chaque groupe de 4 bits en décimal
    l = 0
    Conversion = []
    while l != len(liste_conversion):
        place = 0
        max = len(liste_conversion[l]) - 1
        conversion = 0
        while len(liste_conversion[l]) != place:
            if int(liste_conversion[l][place]) == 1:
                mult = 2 ** max
                max -= 1
                place += 1
                conversion = mult + conversion
            else:
                max -= 1
                place += 1
        conversion = str(conversion)
        L = list(conversion)
        L = list(map(int, L))
        Conversion.append(L)
        l += 1
    # changer ce qui est au-dessus de 9 en lettres
    h = 0
    while h != len(Conversion):
        if len(Conversion[h]) > 1:
            w = Conversion[h][1]
            list_lettres = ['a','b','c','d','e','f']
            Conversion[h] = list_lettres[w]
            h += 1
        else:
            h += 1
    # La liste de liste redevient une liste normale
    Flat_Conversion = []
    for item in Conversion:
        Flat_Conversion += item
    Conversion = Flat_Conversion
    # Conversion de la liste en chaine de caractères
    CONVERSION = ''.join(str(elem) for elem in Conversion)
    return CONVERSION

def hex_to_deci(number):
    # initialisation de la liste
    number = str(number)
    liste = list(number)
    # regarder si il y a des lettres est les convertir en chiffres
    h = 0
    t = 0
    liste_changement = ["a","10","b","11","c","12","d","13","e","14","f","15",]
    while h < len(liste):
        if liste[h] == liste_changement[t]:
            liste[h] = liste_changement[t+1]
            t = 0
            h += 1
        elif t == 10:
            t = 0
            h += 1
        else:
            t += 2
    # multiplication des chiffres par des puissances de 16
    liste_int = list(map(int, liste))
    place = 0
    max = len(liste) - 1
    conversion = 0
    while len(liste_int) != place:
        mult = 16 ** max
        conversion = (mult * liste_int[place]) + conversion
        max -= 1
        place += 1
    return conversion


init()

