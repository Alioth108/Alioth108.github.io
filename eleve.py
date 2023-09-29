# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 09:44:59 2023

@author: davyd
"""

from statistics import harmonic_mean
from datetime import date
from typing import Optional, TYPE_CHECKING
from notes.exception import ControleInexistantError, ControleDejaNoteError, NoteHorsLimitesError, ControleNonNoteError

if TYPE_CHECKING:
    from notes.promotion import Promotion
    from notes.controle import Controle
    
  

class Eleve:
    """
    Cette classe représente un élève.

    :ivar nom: Le nom de l'élève.
    :vartype nom: str
    :ivar promotion: La promotion à laquelle appartient l'élève.
    :vartype promotion: Optional['Promotion']
    :ivar prenom: Le prénom de l'élève.
    :vartype prenom: str
    :ivar date_naissance: La date de naissance de l'élève.
    :vartype date_naissance: date
    :ivar genre: Le genre de l'élève.
    :vartype genre: str
    :ivar notes: Un dictionnaire contenant les notes de l'élève pour chaque contrôle.
    :vartype notes: dict['Controle', float]
    """
    
    nom : str
    promotion : Optional['Promotion']
    prenom : str
    date_naissance : date
    genre : str
    notes:dict['Controle',float]
    
    def __init__(self, nom: str, prenom: int, date_naissance: date, genre : str):
        """
        Initialise un objet Élève.

        :param nom: Le nom de l'élève.
        :type nom: str
        :param prenom: Le prénom de l'élève.
        :type prenom: str
        :param date_naissance: La date de naissance de l'élève.
        :type date_naissance: date
        :param genre: Le genre de l'élève.
        :type genre: str
        """
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.genre = genre
        self.notes = {}
        
    def __str__(self) -> str:
        """
        Renvoie une représentation en chaîne de caractères de l'élève.

        :return: Le nom complet de l'élève.
        :rtype: str
        """
        return f'{self.nom} {self.prenom}'
    
    
    def ajouter_note(self, controle, note):
        """
        Ajoute une note pour un contrôle donné.

        :param controle: Le contrôle pour lequel ajouter la note.
        :type controle: Controle
        :param note: La note à ajouter.
        :type note: float
        :raises ControleInexistantError: Si le contrôle n'existe pas dans la promotion.
        :raises ControleDejaNoteError: Si le contrôle a déjà été noté pour l'élève.
        :raises NoteHorsLimitesError: Si la note n'est pas comprise entre 0 et 20.

        Exemple d'utilisation :
        
        >>> eleve = Eleve("John", "Doe", date(2000, 1, 1), "Masculin")
        >>> controle = Controle("Mathématiques", 10)  # Créez un objet Controle
        >>> eleve.ajouter_note(controle, 15.5)  # Ajoutez une note
        """

        if controle not in self.promotion.controles:
            raise ControleInexistantError(f"Le contrôle {controle} n'existe pas dans la promotion {self.promotion.nom}")

        if controle in self.notes:
            raise ControleDejaNoteError(f"Le contrôle {controle} a déjà été noté pour l'élève {self}")

        if not 0 <= note <= 20:
            raise NoteHorsLimitesError("La note doit être comprise entre 0 et 20")
            
        self.notes[controle] = note
        
    def modifier_note(self, controle, note):
        """
    Modifie une note existante pour un contrôle donné.

    :param controle: Le contrôle pour lequel modifier la note.
    :type controle: Controle
    :param note: La nouvelle note.
    :type note: float
    :raises NoteHorsLimitesError: Si la note n'est pas comprise entre 0 et 20.
    :raises ControleInexistantError: Si le contrôle n'existe pas dans la promotion.
    :raises ControleNonNoteError: Si le contrôle n'a pas encore été noté pour l'élève.

    Cette méthode permet de modifier la note d'un contrôle déjà existant pour un élève donné. Elle vérifie d'abord si le contrôle existe dans la promotion de l'élève, puis si la note est dans la plage valide de 0 à 20. Si le contrôle n'a pas encore été noté, il lèvera une exception.

    Exemple d'utilisation :

    >>> eleve = Eleve("Alice", "Smith", date(2002, 3, 3), "Féminin")
    >>> controle1 = Controle("Mathématiques", 10)
    >>> eleve.ajouter_note(controle1, 15.0)  # Ajoute une note initiale
    >>> eleve.modifier_note(controle1, 18.5)  # Modifie la note existante
    >>> eleve.modifier_note(controle1, 22.0)
    Traceback (most recent call last):
        ...
    NoteHorsLimitesError: La note doit être comprise entre 0 et 20
    >>> controle2 = Controle("Histoire", 5)
    >>> eleve.modifier_note(controle2, 12.0)
    Traceback (most recent call last):
        ...
    ControleNonNoteError: Le contrôle Histoire n'a pas encore été noté pour l'élève Alice Smith
    """
        if controle in self.notes:
            if not 0 <= note <= 20:
                raise NoteHorsLimitesError("La note doit être comprise entre 0 et 20")
            
        if controle not in self.promotion.controles:
               raise ControleInexistantError(f"Le contrôle {controle} n'existe pas dans la promotion {self.promotion.nom}")
            
        if controle not in self.notes:
            raise ControleNonNoteError(f"Le contrôle {controle} n'a pas encore été noté pour l'élève {self}")
            
        self.notes[controle] = note
    
    
    def moyenne(self, matiere=None) -> float:
        """
    Calcule la moyenne des élèves sur ce contrôle.

    :return: La moyenne des élèves sur ce contrôle.
    :rtype: float

    Exemple d'utilisation :

    >>> controle = Controle("Mathématiques", date(2023, 9, 30), "Mathématiques", 2)
    >>> promotion = Promotion(...)
    >>> eleve1 = Eleve("Jane", "Doe", date(2001, 2, 2), "Féminin")
    >>> eleve2 = Eleve("John", "Smith", date(2002, 5, 10), "Masculin")
    >>> eleve1.notes[controle] = 18.0
    >>> eleve2.notes[controle] = 16.5
    >>> promotion.ajouter_eleve(eleve1)
    >>> promotion.ajouter_eleve(eleve2)
    >>> controle.promotion = promotion
    >>> moyenne = controle.moyenne()
    >>> moyenne
    17.25
    """
    
        
        if matiere:
            notes = [note for controle, note in self.notes.items() if controle.matiere == matiere]
        else:
            notes = list(self.notes.values())
        
        if not notes:
            if matiere:
                raise ZeroDivisionError(f"Aucune note disponible pour la matière spécifiée ({matiere}).")
            else:
                raise ZeroDivisionError("Aucune note disponible pour la moyenne de l'élèvé.")
        
        else:
            total_points = sum(note * controle.coefficient for controle, note in self.notes.items())
            total_coefficients = sum(controle.coefficient for controle in self.notes.keys())
            return float(total_points / total_coefficients)
    
