from .objects import MatiereCoefficient, Matiere


from datetime import datetime
from typing import Union


def frenchToEnglish(month: str) -> str:
    """
    Converti un mois en français en anglais

    :param month: Le mois à convertir
    :return: Le mois converti
    """
    MONTHS = {
        'janvier': 'January',
        'février': 'February',
        'mars': 'March',
        'avril': 'April',
        'mai': 'May',
        'juin': 'June',
        'juillet': 'July',
        'août': 'August',
        'septembre': 'September',
        'octobre': 'October',
        'novembre': 'November',
        'décembre': 'December'
    }
    return MONTHS.get(month.lower(), month)


def stringToDatetime(date: str) -> datetime:
    """
    Converti une date en string en datetime
    
    :param date: La date à convertir
    :return: La date convertie
    """
    date_parts = date.split()
    date_parts[1] = frenchToEnglish(date_parts[1])
    date = ' '.join(date_parts).replace("à", "")
    return datetime.strptime(date, "%d %B %Y %H:%M")


def getMatiere(matieres: list[MatiereCoefficient], matiere: str) -> Union[MatiereCoefficient, None]:
    """
    Récupère une matière dans une liste de matières

    :param matieres: La liste de matières
    :param matiere: La matière à récupérer
    :return: La matière récupérée
    """
    for m in matieres:
        if m.code == matiere:
            return m
    return None


def getCompetenceByMatiere(matieres: list[Matiere], matiere: str) -> list[str]:
    """
    Récupère les compétences d'une matière

    :param matieres: La liste de matières
    :param matiere: La matière
    :return: Les compétences de la matière
    """
    for m in matieres:
        if m.matiere == matiere:
            return m

    return []
