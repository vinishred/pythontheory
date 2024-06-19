from entities.Energie import Energie

class Voiture:

    _marque : str
    _modele : str
    _couleur : str
    _immatriculation : str
    _energie : Energie

    def __init__(self, marque, modele, couleur, immatriculation, energie):
        self._marque = marque
        self._modele = modele
        self._couleur = couleur
        self._immatriculation = immatriculation
        self._energie = energie
    
    def _get_marque(self):
        return self._marque
    def _set_marque(self, marque : str):
        if type(marque) is not str:
            raise TypeError("Le marque doit être une chaîne de caractères")
        else:
            self._marque = marque

    def _get_modele(self):
        return self._modele
    def _set_modele(self, modele : str):
        if type(modele) is not str:
            raise TypeError("Le modele doit être une chaîne de caractères")
        else:
            self._modele = modele

    def _get_couleur(self):
        return self._couleur

    def _set_couleur(self, couleur : str):
        if type(couleur) is not str:
            raise TypeError("La couleur doit être une chaîne de caractères")
        else:
            self._couleur = couleur

    def _get_immatriculation(self):
        return self._immatriculation
    
    def _set_immatriculation(self, immatriculation : str):
        if type(immatriculation) is not str:
            raise TypeError("L'immatriculation doit être une chaîne de caractères")
        else:
            self._immatriculation = immatriculation

    def _get_energie(self):
        return self._energie

    def _set_energie(self, energie : Energie):
        if type(energie) is not Energie:
            raise TypeError("L'energie doit être un int")
        else:
            self._energie = energie

    marque = property(_get_marque, _set_marque)
    modele = property(_get_modele, _set_modele)
    couleur = property(_get_couleur, _set_couleur)
    immatriculation = property(_get_immatriculation, _set_immatriculation)
    energie = property(_get_energie, _set_energie)
    
    
