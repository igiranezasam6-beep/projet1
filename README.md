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
