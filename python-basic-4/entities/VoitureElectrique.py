from entities.Energie import Energie
from entities.Voiture import Voiture

class VoitureElectrique(Voiture):
    def __init__(self, marque, modele, couleur, immatriculation):
        super().__init__(marque, modele, couleur, immatriculation, Energie.ELECTRIQUE)