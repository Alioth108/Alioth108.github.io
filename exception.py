#Exception Eleve
class ControleInexistantError(ValueError):
    pass

class ControleDejaNoteError(ValueError):
    pass

class NoteHorsLimitesError(ValueError):
    pass

class ControleNonNoteError(ValueError):
    pass


#Exception pour Promotion
class EleveDejaDansLaPromotionError(ValueError):
    pass

class ControleDejaDansLaPromotionError(ValueError):
    pass