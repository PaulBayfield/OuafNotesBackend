# OuafNotesBackend

OuafNotes est la célèbre application de visualisation des notes et notamment des moyennes des élèves de l'IUT RCC (Reims-Châlons-Charleville).  
Développé par [Lucas Debeve](https://github.com/LucasDebeve/ouaf-notes), pour la v2 l'application a été entièrement repensée et réécrite, pour une meilleure expérience utilisateur et une meilleure maintenabilité.  


# Installation

## Prérequis

- Python

## Configuration

- Créer un fichier `.env` à la racine du projet
- Ajouter les variables suivantes :
```
SERVICE_URL = 

FLASK_SERVER_NAME = 
FLASK_SECRET_KEY = 
```

> [!NOTE]
> - `SERVICE_URL` : URL de l'intranet de l'IUT RCC
> - `FLASK_SERVER_NAME` : URL du serveur
> - `FLASK_SECRET_KEY` : Clé secrète pour Flask


# Utilisation

- Création d'un environnement virtuel
```bash
python -m venv venv
```

- Activation de l'environnement virtuel
```bash
source venv/bin/activate
```

- Installation des dépendances
```bash
pip install -r requirements.txt
```

- Lancement du serveur
```bash
python app.py
```

> [!WARNING]  
> En production, il est recommandé d'utiliser un serveur WSGI tel que Gunicorn ou Hypercorn.  
> 
> Exemple avec Gunicorn :
> ```bash
> gunicorn -w 2 -b 0.0.0.0 app:app
> ```


# Réponse de l'API
```json
{
    "success": true,
    "profil": {
        "firstname": "J",
        "lastname": "C",
        "raw": "j.c",
    },
    "matieres": [],
    "absences": [],
    "competences": []
}
```

> ### Modèle pour les matières
> ```json
> {
>     "code": "R3.01",
>     "name": "Développement web",
>     "raw": "R3.01 | Développement web",
>     "coef": 1.0,
>     "prof": "J C",
>     "competences": [
>         {
>             "coefficient": 15,
>             "name": "Réaliser",
>             "id": 1
>         },
>         {
>             "coefficient": 5,
>             "name": "Optimiser",
>             "id": 2
>         },
>         {
>             "coefficient": 5,
>             "name": "Administrer",
>             "id": 3
>         },
>         {
>             "coefficient": 10,
>             "name": "Gérer",
>             "id": 4
>         }
>     ],
>     "notes": [
>         {
>             "coefficient": 1.0,
>             "date": "12 octobre 2023",
>             "evaluation": "PHP",
>             "max": 20.0,
>             "mean": 14.42,
>             "min": 0.0,
>             "note": 19.0,
>             "rang": "13 / 88",
>             "rangCurrent": 13,
>             "rangMax": 88
>         },
>         {
>             "coefficient": 1.0,
>             "date": "19 octobre 2023",
>             "evaluation": "Javascript",
>             "max": 20.0,
>             "mean": 13.05,
>             "min": 0.0,
>             "note": 19.8,
>             "rang": "4 / 88",
>             "rangCurrent": 4,
>             "rangMax": 88
>         }
>     ],
> },
> ```
> 
> ## Modèle pour les absences
> ```json
> {
>     "matiere": "R3.01",
>     "date": "12/10/2023",
>     "justifiee": true,
>     "saisie": "j C"
> }
> ```
> 
> ## Modèle pour les compétences
> ```json
> {
>     "name": "Réaliser",
>     "id": 1
> }
> ```

# Crédits

- L'API à été entièrement développée par [Paul Bayfield](https://github.com/PaulBayfield).  
  
- Merci à [LockBlock-dev](https://github.com/LockBlock-dev) pour la première version de la connexion à l'intranet l'IUT RCC, faite en JavaScript.
