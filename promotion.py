# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 10:39:28 2023

@author: davyd
"""

from statistics import mean
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from notes.controle import Controle
    from notes.eleve import Eleve
    
from notes.exception import EleveDejaDansLaPromotionError, ControleDejaDansLaPromotionError

class Promotion:
    """
    Cette classe représente une promotion d'élèves.

    :ivar nom: Le nom de la promotion.
    :vartype nom: str
    :ivar annee: L'année de la promotion.
    :vartype annee: int
    :ivar nom_prof: Le nom du professeur principal de la promotion.
    :vartype nom_prof: str
    :ivar controles: La liste des contrôles associés à la promotion.
    :vartype controles: list[Controle]
    :ivar eleves: La liste des élèves de la promotion.
    :vartype eleves: list[Eleve]
    """
    
    nom : str
    annee : int
    nom_prof : str
    controles : list
    eleves : list

    def __init__(self, nom : str, annee : int, nom_prof : str):
        """
        Initialise un objet Promotion.

        :param nom: Le nom de la promotion.
        :type nom: str
        :param annee: L'année de la promotion.
        :type annee: int
        :param nom_prof: Le nom du professeur principal de la promotion.
        :type nom_prof: str
        """
        self.nom = nom
        self.annee = annee
        self.nom_prof = nom_prof
        self.controles = []
        self.eleves = []

    
    def __str__(self) -> str:
        """
        Ajoute un élève à la promotion.

        :param eleve: L'élève à ajouter.
        :type eleve: Eleve
        :raises EleveDejaDansLaPromotionError: Si l'élève est déjà dans la promotion.
        """
        return f'{self.nom} ({self.annee})'
        
        
    def ajouter_eleve(self, eleve):
        """
        Ajoute un élève à la promotion.

        :param eleve: L'élève à ajouter.
        :type eleve: Eleve
        :raises EleveDejaDansLaPromotionError: Si l'élève est déjà dans la promotion.
        
        Exemple d'utilisation :

        >>> promotion = Promotion("Promo 2023", 2023, "Professeur Principal")
        >>> eleve1 = Eleve("Alice", "Smith", date(2002, 3, 15), "Féminin")
        >>> eleve2 = Eleve("Bob", "Johnson", date(2001, 5, 7), "Masculin")
        >>> promotion.ajouter_eleve(eleve1)
        >>> promotion.ajouter_eleve(eleve1)  # Cette ligne générera une exception EleveDejaDansLaPromotionError car l'élève est déjà dans la promotion.
        >>> eleve1.promotion  # Vérification que l'élève a bien été ajouté à la promotion.
        Promotion(Promo 2023, 2023)
        """
        if eleve in self.eleves:
            raise EleveDejaDansLaPromotionError(f"L'élève {eleve} est déjà dans la promotion {self.nom}")
            
        self.eleves.append(eleve)
        eleve.promotion = self

    def ajouter_controle(self, controle):
        """
        Ajoute un contrôle à la promotion.
    
        :param controle: Le contrôle à ajouter.
        :type controle: Controle
        :raises ControleDejaDansLaPromotionError: Si le contrôle est déjà enregistré dans la promotion.
    
        Exemple d'utilisation :
    
        >>> promotion = Promotion("Promo 2023", 2023, "Professeur Principal")
        >>> controle1 = Controle("Mathématiques", date(2023, 9, 30), "Mathématiques", 2)
        >>> controle2 = Controle("Histoire", date(2023, 10, 5), "Histoire", 1)
        >>> promotion.ajouter_controle(controle1)
        >>> try:
        ...     promotion.ajouter_controle(controle1)  # Cette ligne générera une exception ControleDejaDansLaPromotionError car le contrôle est déjà enregistré dans la promotion.
        ... except ControleDejaDansLaPromotionError as e:
        ...     import traceback
        ...     traceback.print_exc()  # Afficher la trace de la stack (traceback).
        Traceback (most recent call last):
            ...
        ControleDejaDansLaPromotionError: Le contrôle Histoire est déjà enregistré dans la promotion Promo 2023
        >>> controle1.promotion  # Vérification que le contrôle a bien été ajouté à la promotion.
        Promotion(Promo 2023, 2023)
    """
        if controle in self.controles:
            raise ControleDejaDansLaPromotionError(f"Le contrôle {controle} est déjà enregistré dans la promotion {self.nom}")
            
        self.controles.append(controle)
        controle.promotion = self



    def moyenne(self, matiere=None) -> float:
        """
        Calcule la moyenne des élèves dans la promotion.
    
        :param matiere: La matière pour laquelle calculer la moyenne (facultatif).
        :type matiere: str
        :return: La moyenne des élèves.
        :rtype: float
        :raises ZeroDivisionError: Si aucune note n'est disponible pour le calcul de la moyenne.
    
        Exemple d'utilisation :
    
        >>> promotion = Promotion("Promo 2023", 2023, "Professeur Principal")
        >>> eleve1 = Eleve("Alice", "Doe", date(2003, 5, 15), "Féminin")
        >>> eleve2 = Eleve("Bob", "Smith", date(2002, 9, 2), "Masculin")
        >>> controle1 = Controle("Mathématiques", date(2023, 9, 30), "Mathématiques", 2)
        >>> controle2 = Controle("Histoire", date(2023, 10, 5), "Histoire", 1)
        >>> eleve1.ajouter_note(controle1, 18.0)
        >>> eleve2.ajouter_note(controle1, 16.5)
        >>> promotion.ajouter_eleve(eleve1)
        >>> promotion.ajouter_eleve(eleve2)
        >>> promotion.ajouter_controle(controle1)
        >>> promotion.ajouter_controle(controle2)
        >>> promotion.moyenne("Mathématiques")
        17.25
        >>> promotion.moyenne("Histoire")
        0.0  # Erreur : Aucune note disponible pour la matière spécifiée (Histoire).
        >>> promotion.moyenne()
        8.625
    """
        notes = []
        for eleve in self.eleves:
            try:
                if matiere:
                    note = eleve.moyenne(matiere)
                else:
                    note = eleve.moyenne()

                notes.append(note)
                
            except ZeroDivisionError:
                pass  
                
        
        if not notes:
            if matiere:
                raise ZeroDivisionError(f"Aucune note disponible pour la matière spécifiée ({matiere}).")
            else:
                raise ZeroDivisionError("Aucune note disponible pour la moyenne de la promotion.")
            
        return float(mean(notes)) 
        
        
    def classement(self) -> tuple[int,"Eleve"]:
        """
        Classe les élèves de la promotion en fonction de leur moyenne.
    
        :return: Une liste de tuples contenant la position dans le classement et l'élève correspondant.
        :rtype: List[Tuple[int, Eleve]]
    
        Exemple d'utilisation :
    
        >>> promotion = Promotion("Promo 2023", 2023, "Professeur Principal")
        >>> eleve1 = Eleve("Alice", "Doe", date(2003, 5, 15), "Féminin")
        >>> eleve2 = Eleve("Bob", "Smith", date(2002, 9, 2), "Masculin")
        >>> controle1 = Controle("Mathématiques", date(2023, 9, 30), "Mathématiques", 2)
        >>> controle2 = Controle("Histoire", date(2023, 10, 5), "Histoire", 1)
        >>> eleve1.ajouter_note(controle1, 18.0)
        >>> eleve2.ajouter_note(controle1, 16.5)
        >>> promotion.ajouter_eleve(eleve1)
        >>> promotion.ajouter_eleve(eleve2)
        >>> promotion.ajouter_controle(controle1)
        >>> promotion.ajouter_controle(controle2)
        >>> classement = promotion.classement()
        >>> for position, eleve in classement:
        ...     print(f"Position {position}: {eleve}")
        Position 1: Alice Doe
        Position 2: Bob Smith
    """
    
        eleves_classement = [(eleve.moyenne(), eleve) for eleve in self.eleves ]
        eleves_classement.sort(key=lambda x: x[0], reverse=True)

        classement_final = []
        position = 1

        for i, (moyenne, eleve) in enumerate(eleves_classement):
            if i > 0 and moyenne < eleves_classement[i - 1][0]:
                position = i + 1
            classement_final.append((position, eleve))

        return classement_final
    

    def matieres(self) -> list[str]:
        """
        Récupère la liste des matières enseignées dans la promotion.
    
        :return: Une liste de noms de matières uniques.
        :rtype: List[str]
    
        Exemple d'utilisation :
    
        >>> promotion = Promotion("Promo 2023", 2023, "Professeur Principal")
        >>> controle1 = Controle("Mathématiques", date(2023, 9, 30), "Mathématiques", 2)
        >>> controle2 = Controle("Histoire", date(2023, 10, 5), "Histoire", 1)
        >>> promotion.ajouter_controle(controle1)
        >>> promotion.ajouter_controle(controle2)
        >>> matieres = promotion.matieres()
        >>> matieres
        ['Mathématiques', 'Histoire']
    """
        matieres = set()
        for controle in self.controles:
            matieres.add(controle.matiere)
        return list(matieres)



