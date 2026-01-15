# EduBurundi - Plateforme d'exercices interactifs

![EduBurundi](https://img.shields.io/badge/EduBurundi-Education-blue)
![Python](https://img.shields.io/badge/Python-3.9+-green)
![Flask](https://img.shields.io/badge/Flask-3.0-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Description

EduBurundi est une plateforme éducative web destinée aux élèves du post-fondamental au Burundi (collège et lycée). Elle permet un accès facile à des exercices, corrigés, vidéos pédagogiques et discussions, tout en facilitant l'interaction entre enseignants et apprenants.

## Fonctionnalités

### 1. Espace Enseignants
- Création de compte vérifié
- Téléversement d'exercices par matière, classe et thème
- Ajout de corrigés séparés ou intégrés
- Accès aux statistiques de consultation
- Réponse aux questions des élèves

### 2. Espace Élèves
- Création de compte personnel
- Navigation par matière, niveau et sujet
- Consultation et téléchargement d'exercices et corrigés
- Accès à des vidéos explicatives
- Possibilité de poser des questions sous chaque exercice

### 3. Chatbot d'Assistance
- Aide à la navigation sur le site
- Réponses aux questions fréquentes
- Suggestions de contenus selon le niveau scolaire

### 4. Forum de Discussion
- Forums thématiques par matière ou niveau
- Modération par enseignants ou administrateurs
- Espace d'entraide entre élèves

### 5. Support Multilingue
- Français (par défaut)
- Kirundi (optionnel)
- Anglais (optionnel)

## Matières Disponibles

- Mathématiques
- Physique
- Chimie
- Biologie
- Français
- Anglais
- Kirundi
- Histoire
- Géographie
- Économie
- Philosophie
- Informatique
- Éducation Civique
- Sciences Sociales

## Niveaux Scolaires

- 7ème année
- 8ème année
- 9ème année
- 10ème année (1ère)
- 11ème année (2ème)
- 12ème année (3ème)
- 13ème année (Terminale)

## Installation

### Prérequis

- Python 3.9 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Cloner le dépôt**
```bash
git clone https://github.com/votre-repo/eduburundi.git
cd eduburundi
```

2. **Créer un environnement virtuel**
```bash
python -m venv venv
source venv/bin/activate  # Sur Linux/Mac
# ou
venv\Scripts\activate  # Sur Windows
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Initialiser la base de données**
```bash
flask init-db
```

5. **Créer un compte administrateur (optionnel)**
```bash
flask create-admin
```

6. **Créer des données de démonstration (optionnel)**
```bash
flask create-sample-data
```

7. **Lancer l'application**
```bash
python run.py
```

L'application sera accessible à l'adresse : `http://localhost:5000`

## Structure du Projet

```
eduburundi/
├── app/
│   ├── __init__.py          # Configuration de l'application Flask
│   ├── models.py            # Modèles de base de données
│   ├── routes/
│   │   ├── main.py          # Routes principales
│   │   ├── auth.py          # Authentification
│   │   ├── teacher.py       # Espace enseignant
│   │   ├── student.py       # Espace élève
│   │   ├── forum.py         # Forum de discussion
│   │   └── chatbot.py       # Assistant chatbot
│   ├── static/
│   │   ├── css/style.css    # Styles personnalisés
│   │   ├── js/main.js       # JavaScript
│   │   └── uploads/         # Fichiers téléversés
│   └── templates/           # Templates HTML
├── config.py                # Configuration
├── requirements.txt         # Dépendances Python
├── run.py                   # Point d'entrée
└── README.md               # Documentation
```

## Technologies Utilisées

- **Backend**: Python, Flask, Flask-SQLAlchemy, Flask-Login
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Base de données**: SQLite (peut être migré vers PostgreSQL)
- **Icônes**: Font Awesome
- **Polices**: Google Fonts (Poppins)

## Configuration

Les paramètres de configuration se trouvent dans `config.py`:

- `SECRET_KEY`: Clé secrète pour les sessions
- `SQLALCHEMY_DATABASE_URI`: URL de la base de données
- `UPLOAD_FOLDER`: Dossier pour les fichiers téléversés
- `MAX_CONTENT_LENGTH`: Taille maximale des fichiers (16MB par défaut)
- `BABEL_DEFAULT_LOCALE`: Langue par défaut ('fr')

## Utilisation

### Pour les Enseignants

1. Créez un compte en choisissant le rôle "Enseignant"
2. Attendez la vérification de votre compte par un administrateur
3. Une fois vérifié, accédez à votre tableau de bord
4. Créez des exercices avec énoncés, fichiers et corrigés
5. Répondez aux questions des élèves

### Pour les Élèves

1. Créez un compte en choisissant votre niveau scolaire
2. Parcourez les exercices par matière ou niveau
3. Téléchargez les exercices et corrigés
4. Posez des questions sur les exercices
5. Participez aux discussions sur le forum

## Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Fork le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/nouvelle-fonctionnalite`)
3. Committez vos changements (`git commit -m 'Ajout d'une nouvelle fonctionnalité'`)
4. Push vers la branche (`git push origin feature/nouvelle-fonctionnalite`)
5. Ouvrez une Pull Request

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## Contact

- **Email**: contact@eduburundi.bi
- **Site web**: https://eduburundi.bi

## Remerciements

- Tous les enseignants qui contribuent à la plateforme
- La communauté éducative du Burundi
- Les contributeurs open source

---

Fait avec ❤️ pour l'éducation au Burundi
