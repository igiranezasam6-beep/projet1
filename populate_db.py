import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eduburundi.settings')
django.setup()

from accounts.models import User
from resources.models import Subject, Level, Exercise
from django.core.files.base import ContentFile

def populate():
    print("Populating database...")
    
    # Create Subjects
    subjects = ['Mathématiques', 'Physique', 'Français', 'Anglais', 'Kirundi', 'Chimie', 'Biologie', 'Histoire', 'Géographie']
    for s in subjects:
        Subject.objects.get_or_create(name=s)
    print(f"Created {len(subjects)} subjects.")

    # Create Levels
    levels = ['7ème Fondamentale', '8ème Fondamentale', '9ème Fondamentale', 
              '1ère Post-Fondamentale', '2ème Post-Fondamentale', '3ème Post-Fondamentale', 'Terminale']
    for l in levels:
        Level.objects.get_or_create(name=l)
    print(f"Created {len(levels)} levels.")

    # Create Superuser
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print("Created superuser 'admin' (password: admin123)")

    # Create Teacher
    if not User.objects.filter(username='professeur').exists():
        teacher = User.objects.create_user('professeur', 'prof@example.com', 'prof123', role=User.Role.TEACHER, is_verified=True)
        print("Created teacher 'professeur' (password: prof123)")
    else:
        teacher = User.objects.get(username='professeur')

    # Create Student
    if not User.objects.filter(username='eleve').exists():
        User.objects.create_user('eleve', 'eleve@example.com', 'eleve123', role=User.Role.STUDENT)
        print("Created student 'eleve' (password: eleve123)")

    # Create Dummy Exercise
    math = Subject.objects.get(name='Mathématiques')
    level_1 = Level.objects.get(name='1ère Post-Fondamentale')
    
    if not Exercise.objects.filter(title='Exercice Algèbre 1').exists():
        ex = Exercise(
            title='Exercice Algèbre 1',
            subject=math,
            level=level_1,
            topic='Équations du second degré',
            teacher=teacher
        )
        ex.file.save('algebra.txt', ContentFile("Contenu de l'exercice d'algèbre"))
        ex.save()
        print("Created dummy exercise.")

if __name__ == '__main__':
    populate()
