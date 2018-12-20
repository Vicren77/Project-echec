# -*- coding: utf-8 -*-

pion = u"pion"
tour = u"tour"
fou = u"fou"
cavalier = u"cavalier"
roi = u"roi"
reine = u"reine"

noir = u"noir"
blanc = u"blanc"

vide = u""

class Piece:
    
    def __init__(self, typePiece = vide, couleurPiece = vide):
        """
        Initialisation d'une pièce :
            -> type : (pion, tour, fou, cavalier, roi, reine)
            -> couleur : (noir, blanc)
        """
        self.type = typePiece
        self.couleur = couleurPiece   
        
    def __str__(self):
        """
        Affichage console de la pièce 
        """
        if self.couleur == blanc:
            if self.type == roi:
                return u"\u2654"
            elif self.type == reine:
                return u"\u2655"
            elif self.type == tour:
                return u"\u2656"
            elif self.type == fou:
                return u"\u2657"
            elif self.type == cavalier:
                return u"\u2658"
            else:
                return u"\u2659"
        elif self.couleur == noir:
            if self.type == roi:
                return u"\u265A"
            elif self.type == reine:
                return u"\u265B"
            elif self.type == tour:
                return u"\u265C"
            elif self.type == fou:
                return u"\u265D"
            elif self.type == cavalier:
                return u"\u265E"
            else:
                return u"\u265F"
        return u"*"
        
    def getType(self):
        """
        Renvoit le type de la pièce
        """
        return self.type
    
    def getCouleur(self):
        """
        Renvoit la couleur de la pièce
        """
        return self.couleur
    
    def estMangee(self):
        """
        Action qui détruit les caractéristiques de la pièce et transforme la
        case en case vide
        """
        self.type = vide
        self.couleur = vide
        
    def estCouleur(self, couleur):
        """
        Teste si la pièce est d'une certaine couleur : 
            couleur : couleur à tester
        """
        return self.couleur == couleur
    
    def estVide(self):
        """
        Teste si la pièce est vide ou pas  : renvoit un booléen true si c'est
        le cas
        """
        return self.type == vide
    
    def nonVide(self):
        """
        Teste si la pièce est non vide : renvoit true si c'est le cas
        """
        return self.type != vide

def sontEnnemis(Piece1, Piece2):
    """
    Teste si deux pièces sont ennemies 
    """
    return (Piece1.getCouleur() == blanc and Piece2.getCouleur() == noir) \
        or (Piece1.getCouleur() == noir and Piece2.getCouleur() == blanc)
