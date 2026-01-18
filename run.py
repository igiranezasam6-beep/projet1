#!/usr/bin/env python3
"""
EduBurundi - Plateforme d'exercices interactifs pour élèves du post-fondamental
Run this file to start the application.
"""

from app import create_app, db
from app.models import User, Exercise, ForumCategory, ChatbotFAQ

app = create_app()

@app.shell_context_processor
def make_shell_context():
    """Add objects to Flask shell context for debugging."""
    return {
        'db': db,
        'User': User,
        'Exercise': Exercise,
        'ForumCategory': ForumCategory,
        'ChatbotFAQ': ChatbotFAQ
    }

@app.cli.command('init-db')
def init_db():
    """Initialize the database with default data."""
    from app.routes.forum import create_default_categories
    from app.routes.chatbot import init_default_faqs
    
    db.create_all()
    
    # Check if we need to create default data
    if ForumCategory.query.count() == 0:
        create_default_categories()
        print("Forum categories created.")
    
    if ChatbotFAQ.query.count() == 0:
        init_default_faqs()
        print("Chatbot FAQs created.")
    
    print("Database initialized successfully!")

@app.cli.command('create-admin')
def create_admin():
    """Create an admin user."""
    import getpass
    
    username = input("Username: ")
    email = input("Email: ")
    password = getpass.getpass("Password: ")
    
    admin = User(
        username=username,
        email=email,
        role='admin',
        is_verified=True,
        first_name='Admin',
        last_name='EduBurundi'
    )
    admin.set_password(password)
    
    db.session.add(admin)
    db.session.commit()
    
    print(f"Admin user '{username}' created successfully!")

@app.cli.command('create-sample-data')
def create_sample_data():
    """Create sample exercises for testing."""
    from app.models import SUBJECTS, CLASS_LEVELS
    
    # Create a sample teacher
    teacher = User.query.filter_by(role='teacher').first()
    if not teacher:
        teacher = User(
            username='enseignant_demo',
            email='enseignant@eduburundi.bi',
            role='teacher',
            is_verified=True,
            first_name='Jean',
            last_name='Nkurunziza'
        )
        teacher.set_password('password123')
        db.session.add(teacher)
        db.session.commit()
        print("Sample teacher created.")
    
    # Create sample exercises
    sample_exercises = [
        {
            'title': 'Équations du premier degré',
            'description': 'Exercices sur la résolution des équations du premier degré à une inconnue.',
            'subject': 'mathematiques',
            'class_level': '7eme',
            'theme': 'Algèbre',
            'difficulty': 'facile',
            'content': 'Résoudre les équations suivantes:\n1. 2x + 5 = 11\n2. 3x - 7 = 8\n3. 4(x + 2) = 20',
            'correction_content': 'Solutions:\n1. x = 3\n2. x = 5\n3. x = 3',
            'has_correction': True
        },
        {
            'title': 'Les forces et le mouvement',
            'description': 'Exercices sur les lois de Newton et les forces.',
            'subject': 'physique',
            'class_level': '9eme',
            'theme': 'Mécanique',
            'difficulty': 'moyen',
            'content': 'Exercice 1: Un objet de masse 5kg est soumis à une force de 20N. Calculer son accélération.',
            'correction_content': 'Solution: a = F/m = 20/5 = 4 m/s²',
            'has_correction': True
        },
        {
            'title': 'La conjugaison au passé composé',
            'description': 'Exercices de conjugaison des verbes au passé composé.',
            'subject': 'francais',
            'class_level': '7eme',
            'theme': 'Conjugaison',
            'difficulty': 'facile',
            'content': 'Conjuguez les verbes suivants au passé composé:\n1. Je (manger)\n2. Nous (partir)\n3. Elles (finir)',
            'correction_content': '1. J\'ai mangé\n2. Nous sommes partis\n3. Elles ont fini',
            'has_correction': True
        }
    ]
    
    for ex_data in sample_exercises:
        existing = Exercise.query.filter_by(title=ex_data['title']).first()
        if not existing:
            exercise = Exercise(**ex_data, author_id=teacher.id)
            db.session.add(exercise)
    
    db.session.commit()
    print("Sample exercises created.")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
