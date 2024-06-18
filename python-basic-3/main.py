#création d'un dictionnaire dans lequel chaque clé est unique
mon_dictionnaire : dict = {"nom" : "Vincent", "age" : 24, "taille" : 1.75, "ville" : "Francheville"}
# print(mon_dictionnaire.get("nom"))

#on veut ajouter un attribut
mon_dictionnaire["poids"] = 75
#ou
mon_dictionnaire.update({"poids" : 75})
# print(mon_dictionnaire)

#on veut modifier un attribut
mon_dictionnaire["poids"] = 80
# print(mon_dictionnaire)

#on veut supprimer un attribut
del mon_dictionnaire["ville"]
# print(mon_dictionnaire)
#ou
# mon_dictionnaire.pop("ville")
# print(mon_dictionnaire)

#vider un dictionnaire
# mon_dictionnaire.clear()
# print(mon_dictionnaire)

#pour boucler sur un dictionnaire on utilise la boucle for
# for cle, valeur in mon_dictionnaire.items():
#     print("l'attribut: " + cle + " a pour valeur: " + str(valeur))

#Gestion d'erreur

# try :
#     print(mon_dictionnaire["cheveux"])
# except Exception:
#     print("l'attribut n'existe pas dans le dictionnaire")
# finally:
#     print("fin du programme")

#on doit spécialiser nos exceptions pour les erreurs pour se faire le mieux est de déclencher l'erreur pour voir son type
# print(mon_dictionnaire["cheveux"])

# try :
#     print(mon_dictionnaire["cheveux"])
# except KeyError:
#     print("l'attribut n'existe pas dans le dictionnaire")
# finally:
#     print("fin du programme")

#fusionner deux dictionnaires
def fusion_dict():
    dict_un : dict = {"prénom" : "Vincent", "age" : 42, "taille" : 1.75, "ville" : "Francheville"}
    dict_deux : dict = {"nom" : "Callarec", "poids" : 75, "yeux" : "bleus"}
    #1ere ecriture
    dict_un.update(dict_deux)
    print(dict_un)

    #2eme ecriture
    # new_dict : dict = {**dict_un, **dict_deux}

# fusion_dict()

#mettre deux listes dans un dictionnaire
def fusion_list():
    list_key : list = ['nom', 'age', 'taille', 'ville']
    list_value : list = ['Vincent', 24, 1.75, 'Francheville']
    #1ere ecriture
    # mon_dict : dict = {}
    # if len(list_key) == len(list_value):
    #     for index,value in enumerate(list_key):
    #         mon_dict[value] = list_value[index]
    #     print(mon_dict)
    # else:
    #     print("les listes ne sont pas de la meme longueur")

    #2eme ecriture
    mon_dict : dict = dict(zip(list_key, list_value))
    print(mon_dict)

# fusion_list()

#afficher les clefs ainsi que les valeurs d'un dictionnaire et absence de valeur si valeur égale à 0
def display_key_values():
    mon_dict : dict = {'Zero': 0, 'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9}
    for cle, valeur in mon_dict.items():
        if valeur != 0:
            print(f"la clé {cle} possède la valeur de {valeur}")
        else:
            print(f"la clé {cle} ne possède pas de valeur")

# display_key_values()

def display_keys(key: str):
    dict_sample : dict = {"nom": "Toto", "prenom": "tarte", "age ": 10}
    #1ere méthode
    # try:
    #     print(f"la clé {key} possède la valeur de {dict_sample.get(key)}")
    # except KeyError:
    #     print(f"la clé {key} n'existe pas dans le dictionnaire")
    # except Exception:
    #     print("une erreur est survenue")

    #2eme ecriture
    print(dict_sample.get(key, "la clé n'existe pas"))
# display_keys("valeur")

def rename_key_dict(new_key: str, old_key: str):
    dict_sample : dict = {"nom": "Toto", "plat favori": "tarte", "age ": 10}
    if old_key in dict_sample.keys() and new_key not in dict_sample.keys():
        dict_sample[new_key] = dict_sample.pop(old_key)
        print(dict_sample)
    else :
        print("il existe un problème de clés dans le dictionnaire")

# rename_key_dict("prénom", "nomage")

#création d'un set qui est une liste dans laquelle on ne peut mettre qu'une seule fois un élément
mon_set : set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

#création d'un tuple
mon_tuple : tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
