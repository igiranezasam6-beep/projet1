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

