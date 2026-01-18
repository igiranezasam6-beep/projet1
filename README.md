## EduBurundi – Plateforme d’exercices interactifs (MVP)

MVP web en **Django** pour publier/consulter des exercices (avec corrigés, liens vidéo), poser des questions, discuter via un forum, et utiliser un petit chatbot d’assistance.

### Fonctionnalités incluses

- **Comptes**
  - Inscription **élève** (accès immédiat)
  - Inscription **enseignant** (compte **à vérifier** par l’admin avant dépôt)
- **Exercices**
  - Navigation/filtre par **matière**, **niveau**, **thème**, recherche texte
  - Téléversement (enseignants vérifiés), téléchargement exercice/corrigé, lien vidéo
  - **Questions** sous chaque exercice
- **Forum**
  - Sujets + réponses (auth requis pour poster)
- **Chatbot**
  - FAQ simple (mots-clés) + suggestions d’exercices par niveau

### Lancer en local

Prérequis: Python 3.12+

```bash
python3 -m pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver 0.0.0.0:8000
```

Ensuite:
- Site: `http://localhost:8000/`
- Admin: `http://localhost:8000/admin/`

### Vérification des enseignants

1. L’enseignant crée son compte via `Créer un compte → Enseignant`
2. Un admin ouvre `Admin → Profiles` et coche **is_verified**
3. L’enseignant peut ensuite publier via `Exercices → Publier un exercice`

### Stockage des fichiers

Les fichiers téléversés sont servis en dev via `MEDIA_URL`/`MEDIA_ROOT` (dossier `media/`).

# EduBurundi - Plateforme d'exercices interactifs

Prototype statique pour illustrer les principales fonctionnalites d'une
plateforme d'exercices interactifs destinee aux eleves du post-fondamental au
Burundi.

## Fonctionnalites couvertes

- Espace enseignants: publication d'exercices, corriges et liens video.
- Espace eleves: recherche par matiere, niveau, theme et questions par exercice.
- Chatbot d'assistance: reponses aux questions frequentes et suggestions.
- Forum d'entraide: discussions par matiere/niveau avec reponses.
- Multilingue: francais, anglais, kirundi (interface de base).

## Utilisation

1. Ouvrir `index.html` dans un navigateur moderne.
2. Les donnees sont stockees dans `localStorage` pour simuler des comptes et
   publications locales.

## Limites

- Aucun backend: toutes les donnees restent dans le navigateur.
- Authentification et moderation non implementees (maquette uniquement).
# EduBurundi

Plateforme d’exercices interactifs pour élèves du post-fondamental au Burundi.

## Objectif
Créer une plateforme web éducative permettant un accès facile à des exercices, corrigés, vidéos pédagogiques et discussions.

## Fonctionnalités
- **Espace Enseignants**: Gestion des exercices et corrigés.
- **Espace Élèves**: Consultation des ressources, vidéos.
- **Chatbot**: Assistance et navigation.
- **Forum**: Espace de discussion et d'entraide.

## Installation
1. `pip install -r requirements.txt`
2. `python manage.py migrate`
3. `python populate_db.py` (Pour ajouter des données de test)
4. `python manage.py runserver`

## Comptes de démonstration
- **Admin**: admin / admin123
- **Enseignant**: professeur / prof123
- **Élève**: eleve / eleve123
