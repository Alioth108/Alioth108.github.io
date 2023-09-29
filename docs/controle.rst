Controle
========

Cette classe représente un contrôle.

Attributs
---------

.. py:attribute:: date

   La date du contrôle.

   :type: date

.. py:attribute:: matiere

   La matière du contrôle.

   :type: str

.. py:attribute:: coefficient

   Le coefficient du contrôle (par défaut : 1).

   :type: int

.. py:attribute:: promotion

   La promotion à laquelle est associé le contrôle.

   :type: Optional['Promotion']

.. py:attribute:: nom

   Le nom du contrôle.

   :type: str

Méthodes
--------

.. py:method:: __init__(nom: str, date: date, matiere: str, coefficient: int=1)

   Initialise un objet Contrôle.

   :param nom: Le nom du contrôle.
   :type nom: str
   :param date: La date du contrôle.
   :type date: date
   :param matiere: La matière du contrôle.
   :type matiere: str
   :param coefficient: Le coefficient du contrôle (par défaut : 1).
   :type coefficient: int
   :noindex:

.. py:method:: __str__()

   Renvoie une représentation en chaîne de caractères du contrôle.

   :return: Une chaîne de caractères représentant le contrôle.
   :rtype: str
   :noindex:

.. py:method:: moyenne()

   Calcule la moyenne des élèves sur ce contrôle.

   :noindex:
   :return: La moyenne des élèves sur ce contrôle.
   :rtype: float
   :noindex:

   Exemple d'utilisation :

.. code-block:: python

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


.. py:method:: recuperer_notes()

   Récupère les notes des élèves pour ce contrôle.

   :noindex:
   :return: Un dictionnaire associant les élèves à leurs notes.
   :rtype: dict["Eleve", float]
