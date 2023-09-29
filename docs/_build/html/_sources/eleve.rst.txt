Eleve
=====

Cette classe représente un élève.

Attributs
---------

.. py:attribute:: nom

   Le nom de l'élève.

   :type: str

.. py:attribute:: promotion

   La promotion à laquelle appartient l'élève.

   :type: Optional['Promotion']

.. py:attribute:: prenom

   Le prénom de l'élève.

   :type: str

.. py:attribute:: date_naissance

   La date de naissance de l'élève.

   :type: date

.. py:attribute:: genre

   Le genre de l'élève.

   :type: str

.. py:attribute:: notes

   Un dictionnaire contenant les notes de l'élève pour chaque contrôle.

   :type: dict['Controle', float]

Méthodes
--------

.. py:method:: __init__(nom: str, prenom: int, date_naissance: date, genre: str)

   Initialise un objet Élève.

   :param nom: Le nom de l'élève.
   :type nom: str
   :param prenom: Le prénom de l'élève.
   :type prenom: str
   :param date_naissance: La date de naissance de l'élève.
   :type date_naissance: date
   :param genre: Le genre de l'élève.
   :type genre: str

.. py:method:: __str__()

   Renvoie une représentation en chaîne de caractères de l'élève.

   :return: Le nom complet de l'élève.
   :rtype: str

.. py:method:: ajouter_note(controle, note)

   Ajoute une note pour un contrôle donné.

   :param controle: Le contrôle pour lequel ajouter la note.
   :type controle: Controle
   :param note: La note à ajouter.
   :type note: float
   :raises ControleInexistantError: Si le contrôle n'existe pas dans la promotion.
   :raises ControleDejaNoteError: Si le contrôle a déjà été noté pour l'élève.
   :raises NoteHorsLimitesError: Si la note n'est pas comprise entre 0 et 20.

   Exemple d'utilisation :

.. code-block:: python

   >>> eleve = Eleve("John", "Doe", date(2000, 1, 1), "Masculin")
   >>> controle = Controle("Mathématiques", 10)  # Créez un objet Controle
   >>> eleve.ajouter_note(controle, 15.5)  # Ajoutez une note

.. py:method:: modifier_note(controle, note)

   Modifie une note existante pour un contrôle donné.

   :param controle: Le contrôle pour lequel modifier la note.
   :type controle: Controle
   :param note: La nouvelle note.
   :type note: float
   :raises NoteHorsLimitesError: Si la note n'est pas comprise entre 0 et 20.
   :raises ControleInexistantError: Si le contrôle n'existe pas dans la promotion.
   :raises ControleNonNoteError: Si le contrôle n'a pas encore été noté pour l'élève.

   Exemple d'utilisation :

.. code-block:: python

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

.. py:method:: moyenne(matiere=None)

   Calcule la moyenne des notes de l'élève.

   :param matiere: La matière pour laquelle calculer la moyenne (facultatif).
   :type matiere: str
   :return: La moyenne des notes.
   :rtype: float
   :raises ZeroDivisionError: Si aucune note n'est disponible pour le calcul de la moyenne.

   Exemple d'utilisation :

.. code-block:: python

   >>> eleve = Eleve("Jane", "Doe", date(2001, 2, 2), "Féminin")
   >>> controle1 = Controle("Mathématiques", 10)
   >>> controle2 = Controle("Histoire", 5)
   >>> eleve.ajouter_note(controle1, 15.0)
   >>> eleve.ajouter_note(controle2, 12.0)
   >>> eleve.moyenne("Mathématiques")
   15.0
   >>> eleve.moyenne()
   13.5
