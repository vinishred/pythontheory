from entities.Energie import Energie
from entities.Voiture import Voiture
from entities.VoitureElectrique import VoitureElectrique

ma_premiere_voiture : Voiture = Voiture("Ford", "Focus", "Bleu", "AB-123-CD", Energie.ELECTRIQUE)
ma_deuxieme_voiture : Voiture = Voiture("Peugeot", "5008", "Bleu", "EF-456-GH", Energie.ESSENCE)

ma_troisième_voiture : Voiture = VoitureElectrique("Ford", "Focus", "Bleu", "AB-123-CD")

print(ma_premiere_voiture._get_energie())