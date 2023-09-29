# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 10:39:28 2023

@author: davyd
"""

from datetime import date
from typing import Optional, TYPE_CHECKING
import numpy as np

if TYPE_CHECKING:
    from notes.promotion import Promotion
    from notes.eleve import Eleve

class Controle:
    """
    Cette classe représente un contrôle.

    :ivar date: La date du contrôle.
    :vartype date: date
    :ivar matiere: La matière du contrôle.
    :vartype matiere: str
    :ivar coefficient: Le coefficient du contrôle (par défaut : 1).
    :vartype coefficient: int
    :ivar promotion: La promotion à laquelle est associé le contrôle.
    :vartype promotion: Optional['Promotion']
    :ivar nom: Le nom du contrôle.
    :vartype nom: str
    """
    
    date : date
    matiere : str
    coefficient : int
    promotion : Optional['Promotion']
    nom : str
    

    def __init__(self, nom : str, date: date, matiere: str, coefficient: int=1):
        """
        Initialise un objet Contrôle.

        :param nom: Le nom du contrôle.
        :type nom: str
        :param date: La date du contrôle.
        :type date: date
        :param matiere: La matière du contrôle.
        :type matiere: str
        :param coefficient: Le coefficient du contrôle (par défaut : 1).
        :type coefficient: int
        """
        self.date = date
        self.matiere = matiere
        self.coefficient = coefficient
        self.nom = nom
        
    def __str__(self) -> str:
        """
        Renvoie une représentation en chaîne de caractères du contrôle.

        :return: Une chaîne de caractères représentant le contrôle.
        :rtype: str
        """
        return f'{self.nom} (matière : {self.matiere})'
    
    #Moyenne des élèves sur ce controle
    def moyenne(self):
        """
        Calcule la moyenne des élèves sur ce contrôle.
        :noindex:
    
        Returns:
            float: La moyenne des élèves sur ce contrôle.
            
        Exemple d'utilisation :

        >>> eleve = Eleve("Jane", "Doe", date(2001, 2, 2), "Féminin")
        >>> controle1 = Controle("Mathématiques", date(2023, 9, 30), "Mathématiques", 2)
        >>> promotion = Promotion("Promo 2023", 2023, "Professeur Principal")
        >>> eleve1 = Eleve("Alice", "Smith", date(2002, 3, 15), "Féminin")
        >>> eleve2 = Eleve("Bob", "Johnson", date(2001, 5, 7), "Masculin")
        >>> eleve1.notes[controle1] = 18.0
        >>> eleve2.notes[controle1] = 16.5
        >>> promotion.ajouter_eleve(eleve1)
        >>> promotion.ajouter_eleve(eleve2)
        >>> controle1.promotion = promotion
        >>> eleve.promotion = promotion
        >>> eleve.ajouter_note(controle1, 15.0)
        >>> eleve.moyenne("Mathématiques")
        15.0
        """
        notes_eleve = self.recuperer_notes()
        total_points = sum(note * eleve.notes[self] for eleve, note in notes_eleve.items())
        total_coefficients = sum(eleve.notes[self] for eleve in notes_eleve.keys())
        return total_points / total_coefficients

    
    def recuperer_notes(self) -> dict["Eleve",float]:
        """
        Récupère les notes des élèves pour ce contrôle.
        :noindex:

        Returns:
            dict[str, float]: Un dictionnaire associant les élèves à leurs notes.
        """
        notes_eleve = {}
        for eleve, note in self.promotion.notes.items():
            if self in note:
                notes_eleve[eleve] = note[self]
        return notes_eleve
    
    
    
    
    