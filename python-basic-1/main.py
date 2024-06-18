#affichage d'une phrase
import math


print("Voici mon premier fichier python !")
# print("Faisons d'abord des additions !")

#somme de deux valeurs
#On type nos paramètres et notre sortie
def sum_two_values(value1: int, value2: int) -> int:
    return value1 + value2

# print ("La somme de deux valeurs fixes est : ", sum_two_values(15, 30))

def sum_two_values_user() -> int:
    #on demande à l'utilisateur de rentrer deux valeurs
    user_value1: int = int(input("Entrez la première valeur: "))
    user_value2: int = int(input("Entrez la deuxième valeur: "))
    return sum_two_values(user_value1, user_value2)

# print ("La somme de deux valeurs saisies par l'utilisateur est : ", sum_two_values_user())

# print("Faisons ensuite des comparaisons !")

#comparaison de deux valeurs
#On type nos paramètres et notre sortie
def compare_two_values(value1: int, value2: int) -> None:
    if (value1 < value2): print (value1 , " est inférieur à " , value2)
    elif (value1 > value2): print (value1 , " est supérieur à " , value2)
    else: print (value1 , " est égal à " , value2)

# compare_two_values(15, 16)

def compare_two_values_user() -> None:
    #on demande à l'utilisateur de rentrer deux valeurs
    user_value1: int = int(input("Entrez la première valeur: "))
    user_value2: int = int(input("Entrez la deuxième valeur: "))
    print ("La comparaison de deux valeurs saisies par l'utilisateur est : ")
    return compare_two_values(user_value1, user_value2)

# compare_two_values_user()

#Teste si personne mineure ou majeure
#On type nos paramètres et notre sortie
def is_major(value1: int) -> None:
    if (value1 < 18): print ("vous êtes mineur.")
    else : print ("vous êtes majeur.")

# is_major(15)

def is_major_user() -> None:
    #on demande à l'utilisateur de rentrer deux valeurs
    age: float = float(input("Entrez votre âge: "))
    if age < 0: 
        print ("age impossible.")
        #retourner à la saisie utilisateur 
        return is_major_user()
    print ("D'après l'âge que vous avez entré: ")
    return is_major(age)

# is_major_user()

#theoreme de pythagore
# print("Faisons le theoreme de pythagore !")
def pythagore(value1: float, value2: float) -> None:
    cote1: float = float(value1**2)
    cote2: float = float(value2**2)
    hypothenuse: float = float(cote1 + cote2)
    print ("la longueur de l'hypothenuse est : ", hypothenuse**0.5)

# pythagore(3, 4)

def pythagore_user() -> None:
    #on demande à l'utilisateur de rentrer deux valeurs
    question= input("connaissez vous l'hypothenuse ? (oui/non): ").strip().lower()
    if (question == 'non'):
        cote1: float = float(input("Entrez la longueur du cote 1: "))
        cote2: float = float(input("Entrez la longueur du cote 2: "))
        print("La longueur de l'hypothenuse est de:" + str(math.sqrt(pow(cote1, 2) + pow(cote2, 2))))

    elif (question == 'oui'):
        hypothenuse: float = float(input("Entrez la longueur de l'hypothenuse: "))
        cote1: float = float(input("Entrez la longueur du premier côté: "))
        print("La longueur du dernier côté est de:" + str(math.sqrt(pow(hypothenuse, 2) - pow(cote1, 2))))

    else: 
        print ("votre choix n'est pas valide !")
        return pythagore_user()

# pythagore_user()

#on fait les factoriels d'un nombre
def factorielle(nombre : int):
    if nombre <= 0:
        return 0
    elif nombre == 1:
        return 1
    else:
        #1ere methode
        # fact = 1
        # for i in range(1, nombre+1):
        #     fact *= i
        # print("Factoriel de ", nombre, " est ", fact)

        #2eme methode
        # print("Factoriel de ", nombre, " est ", math.factorial(nombre))

        #3eme methode
        return nombre * factorielle(nombre - 1)

print(factorielle(5))
