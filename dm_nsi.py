def init():
    print("Bonjours !!")
    print("Bienvenue sur mon programme de Convertion")
    print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
    print("1 : décimal")
    print("2 : binaire")
    print("3 : hexadécimal")
    print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
    choix = int(input("Quel est ton unité de départ ? "))
    number = input("Quel est ton chiffre ? ")
    print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
    if choix == 1:
        print("binaire --> ", deci_to_bin(number))
        print("hexadécimal --> ", bin_to_hex(deci_to_bin(number)))
    elif choix == 2:
        print("décimal --> ", bin_to_deci(number))
        print("héxadécimal --> ", bin_to_hex(number))
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
    # convertion
    place = 0
    max = len(liste)-1
    convertion = 0
    while len(liste) != place:
        if int(liste[place]) == 1:
            mult = 2**max
            convertion = mult + convertion
            max -= 1
            place += 1
        else:
            max -= 1
            place += 1
    return convertion

def deci_to_bin(number):
    # initialisation de la liste
    number = int(number)
    liste = []
    # je convertie comme on convertie sur une feuille donc avec les puissances sur le chiffre 2
    puissance = 1
    while number > 2 ** puissance:
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
    # convertion de la liste en chaine de caractère
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
    # divisition en groupe de 4 bit
    debut = 0
    fin = 4
    liste_convertion = []
    while fin <= len(liste):
        liste_liste = liste[debut:fin]
        liste_convertion.append(liste_liste)
        debut += 4
        fin += 4
    # convertion de chaque groupes de 4 bit en décimal
    l = 0
    Convertion = []
    while l != len(liste_convertion):
        place = 0
        max = len(liste_convertion[l]) - 1
        convertion = 0
        while len(liste_convertion[l]) != place:
            if int(liste_convertion[l][place]) == 1:
                mult = 2 ** max
                max -= 1
                place += 1
                convertion = mult + convertion
            else:
                max -= 1
                place += 1
        convertion = str(convertion)
        L = list(convertion)
        L = list(map(int, L))
        Convertion.append(L)
        l += 1
    # changer ce qui est au dessus de 9 en lettres
    h = 0
    while h != len(Convertion):
        if len(Convertion[h]) > 1:
            w = Convertion[h][1]
            list_lettres = ['a','b','c','d','e','f']
            Convertion[h] = list_lettres[w]
            h += 1
        else:
            h += 1
    # La liste de liste redevien une liste normal
    Flat_Convertion = []
    for item in Convertion:
        Flat_Convertion += item
    Convertion = Flat_Convertion
    # Convertion de la liste en chaine de caractère
    CONVERTION = ''.join(str(elem) for elem in Convertion)
    return CONVERTION

def hex_to_deci(number):
    # initialisation de la liste
    number = str(number)
    liste = list(number)
    # regarder si il y a des lettres est les convertires en chiffres
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
    # multiplication des chiffre par des puissances de 16
    liste_int = list(map(int, liste))
    place = 0
    max = len(liste) - 1
    convertion = 0
    while len(liste_int) != place:
        mult = 16 ** max
        convertion = (mult * liste_int[place]) + convertion
        max -= 1
        place += 1
    return convertion


init()

