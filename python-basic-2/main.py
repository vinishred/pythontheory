#Dans python on utilise plus les listes que les tableaux qui ne sont pas une propriété native en python	
#pour mettre un tableau on doit faire un import 
#import array as arr

#On utilise donc plutot les listes
#afficher une liste
import random
from unidecode import unidecode


maListe = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
maListe.append(11)
maListe.append('Vincent')
maListe.append(['gateau', 'donut'])
# print(maListe)
# print(type(maListe))

# for element in maListe:
#     i = maListe.index(element)
#     print("l'élément à l'index " + str(i) + " est : " + str(element))

#autre méthode
# for index, value in enumerate(maListe):
#     print("l'élément à l'index " + str(index) + " est : " + str(value))

# x: int = 0
# while x < 10:
#     print("mon élément x vaut" + str(x))
#     x = x + 1

def occurence(un_mot : str):
    list_lettre : list[str] = []
    compteur_lettre : list[int] = []
    for element in un_mot:
        # On veut mettre les lettres en minuscule pour pouvoir les compter
        element = element.lower()
        list_lettre.append(element)
        # on veut compter le nombre d'occurence de chaque lettre
        if element in list_lettre:
            compteur_lettre.append(list_lettre.count(element))
    print(compteur_lettre)
# occurence("Vincent")

def display_hundred_int():
    for i in range(10):
        print(i)
# display_hundred_int()


def mention_moyenne():
    nombre_notes : int = 10
    note_aleatoire: float = float(random.uniform(0, 20))
    somme_notes: float = 0
    moyenne_notes: float = 0

    liste_note : list[float] = []
    for note in range(nombre_notes):
        liste_note.append(note_aleatoire)
    
    for note in liste_note:
        somme_notes = somme_notes + note
    
    moyenne_notes = somme_notes / nombre_notes
    print("Vous avez obtenu la moyenne de " + str(moyenne_notes))
    if (moyenne_notes >= 10 and moyenne_notes < 12):
        print("vous avez votre examen sans mention")
    elif (moyenne_notes >= 12 and moyenne_notes < 14):
        print("vous avez votre examen avez la mention assez bien")
    elif (moyenne_notes >= 14 and moyenne_notes < 16):
        print("vous avez votre examen avec la mention bien")
    elif (moyenne_notes >= 16 and moyenne_notes < 18):
        print("vous avez votre examen avec la mention très bien")
    elif (moyenne_notes >= 18 and moyenne_notes < 20):
        print("vous avez votre examen avec les félicitations du jury")
    else:
        print("vous n'avez pas votre examen")


# mention_moyenne()

def display_voyelles():
    un_mot : str = input('Saisissez un mot : ')
    list_voyelles : list[str] = ['a', 'e', 'i', 'o', 'u', 'y']
    # on veut enlever les accents dans notre variable un_mot et on la met en minuscule
    un_mot = unidecode(un_mot).lower()
    compteur : int = 0

    for element in un_mot:
        if element in list_voyelles:
            compteur = compteur + 1

    print('Il y a ' + str(compteur) + ' voyelles dans le mot ' + un_mot)


display_voyelles()

