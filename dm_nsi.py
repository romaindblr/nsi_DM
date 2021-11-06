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
            max -= 1
            place += 1
            convertion = mult + convertion
        else:
            max -= 1
            place += 1
    print("-->",convertion)

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
    Liste = ''.join(str(elem) for elem in liste)
    print("-->",Liste)

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
    print("-->", CONVERTION)

a = int(input("binaire en decimal : "))
bin_to_deci(a)
b = int(input("decimal en binaire : "))
deci_to_bin(b)
c = int(input("binaire en hexadecimal : "))
bin_to_hex(c)

