Promotion
=========

Cette classe représente une promotion.

Attributs
---------

.. py:attribute:: nom

   Le nom de la promotion.

   :type: str

.. py:attribute:: annee

   L'année de la promotion.

   :type: int

.. py:attribute:: nom_prof

   Le nom du professeur responsable de la promotion.

   :type: str

.. py:attribute:: controles

   La liste des contrôles associés à la promotion.

   :type: list

.. py:attribute:: eleves

   La liste des élèves de la promotion.

   :type: list

Méthodes
--------

.. py:method:: __init__(nom: str, annee: int, nom_prof: str)

   Initialise un objet Promotion.

   :param nom: Le nom de la promotion.
   :type nom: str
   :param annee: L'année de la promotion.
   :type annee: int
   :param nom_prof: Le nom du professeur responsable de la promotion.
   :type nom_prof: str

.. py:method:: __str__()

   Renvoie une représentation en chaîne de caractères de la promotion.

   :return: Une chaîne de caractères représentant la promotion.
   :rtype: str

.. py:method:: ajouter_eleve(eleve)

   Ajoute un élève à la promotion.

   :param eleve: L'élève à ajouter.
   :type eleve: Eleve
   :raises EleveDejaDansLaPromotionError: Si l'élève est déjà dans la promotion.

   Exemple d'utilisation :

.. code-block:: python

   >>> promotion = Promotion("Promo 2023", 2023, "Professeur Principal")
   >>> eleve1 = Eleve("Alice", "Smith", date(2002, 3, 15), "Féminin")
   >>> eleve2 = Eleve("Bob", "Johnson", date(2001, 5, 7), "Masculin")
   >>> promotion.ajouter_eleve(eleve1)
   >>> promotion.ajouter_eleve(eleve1)  # Cette ligne générera une exception EleveDejaDansLaPromotionError car l'élève est déjà dans la promotion.
   >>> eleve1.promotion  # Vérification que l'élève a bien été ajouté à la promotion.
   Promotion(Promo 2023, 2023)

.. py:method:: ajouter_controle(controle)

   Ajoute un contrôle à la promotion.

   :param controle: Le contrôle à ajouter.
   :type controle: Controle
   :raises ControleDejaDansLaPromotionError: Si le contrôle est déjà enregistré dans la promotion.

   Exemple d'utilisation :

.. code-block:: python

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

.. py:method:: moyenne(matiere=None)

   Calcule la moyenne des élèves de la promotion.

   :param matiere: La matière pour laquelle calculer la moyenne (facultatif).
   :type matiere: str
   :return: La moyenne des élèves.
   :rtype: float
   :raises ZeroDivisionError: Si aucune note n'est disponible pour le calcul de la moyenne.

    Exemple d'utilisation :
.. code-block:: python
    
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

.. py:method:: classement()

   Génère le classement des élèves de la promotion.

   :return: Un tuple contenant la position dans le classement et l'élève correspondant.
   :rtype: tuple[int, Eleve]

    Exemple d'utilisation :

.. code-block:: python
    
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

.. py:method:: matieres()

   Récupère la liste des matières disponibles dans la promotion.

   :return: Une liste de noms de matières.
   :rtype: list[str]

    Exemple d'utilisation :

.. code-block:: python
    
    >>> promotion = Promotion("Promo 2023", 2023, "Professeur Principal")
    >>> controle1 = Controle("Mathématiques", date(2023, 9, 30), "Mathématiques", 2)
    >>> controle2 = Controle("Histoire", date(2023, 10, 5), "Histoire", 1)
    >>> promotion.ajouter_controle(controle1)
    >>> promotion.ajouter_controle(controle2)
    >>> matieres = promotion.matieres()
    >>> matieres
    ['Mathématiques', 'Histoire']
