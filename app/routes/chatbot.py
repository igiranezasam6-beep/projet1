from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from app import db
from app.models import ChatbotFAQ, Exercise, SUBJECTS, CLASS_LEVELS
import re

chatbot_bp = Blueprint('chatbot', __name__)

# Predefined responses for common queries
CHATBOT_RESPONSES = {
    'salut': "Bonjour ! Je suis l'assistant EduBurundi. Comment puis-je vous aider aujourd'hui ?",
    'bonjour': "Bonjour ! Je suis l'assistant EduBurundi. Comment puis-je vous aider aujourd'hui ?",
    'hello': "Bonjour ! Je suis l'assistant EduBurundi. Comment puis-je vous aider aujourd'hui ?",
    'aide': "Je peux vous aider à :\n- Trouver des exercices par matière ou niveau\n- Naviguer sur le site\n- Répondre aux questions fréquentes\n\nQue souhaitez-vous faire ?",
    'help': "Je peux vous aider à :\n- Trouver des exercices par matière ou niveau\n- Naviguer sur le site\n- Répondre aux questions fréquentes\n\nQue souhaitez-vous faire ?",
    'exercice': "Pour trouver des exercices :\n1. Allez dans 'Exercices' depuis votre tableau de bord\n2. Filtrez par matière, niveau ou difficulté\n3. Cliquez sur un exercice pour le voir\n\nVoulez-vous que je vous suggère des exercices ?",
    'forum': "Le forum vous permet de :\n- Poser des questions à la communauté\n- Aider d'autres élèves\n- Discuter avec des enseignants\n\nAccédez-y via le menu 'Forum'.",
    'compte': "Pour gérer votre compte :\n1. Cliquez sur votre nom en haut à droite\n2. Sélectionnez 'Mon profil'\n3. Modifiez vos informations\n\nBesoin d'aide supplémentaire ?",
    'merci': "Je vous en prie ! N'hésitez pas si vous avez d'autres questions.",
    'thanks': "Je vous en prie ! N'hésitez pas si vous avez d'autres questions.",
    'au revoir': "Au revoir ! Bonne continuation dans vos études !",
    'bye': "Au revoir ! Bonne continuation dans vos études !",
}

# Subject-specific suggestions
SUBJECT_SUGGESTIONS = {
    'math': 'mathematiques',
    'maths': 'mathematiques',
    'mathematique': 'mathematiques',
    'physique': 'physique',
    'chimie': 'chimie',
    'bio': 'biologie',
    'biologie': 'biologie',
    'francais': 'francais',
    'français': 'francais',
    'anglais': 'anglais',
    'english': 'anglais',
    'kirundi': 'kirundi',
    'histoire': 'histoire',
    'geo': 'geographie',
    'géo': 'geographie',
    'geographie': 'geographie',
    'géographie': 'geographie',
    'economie': 'economie',
    'économie': 'economie',
    'philo': 'philosophie',
    'philosophie': 'philosophie',
    'info': 'informatique',
    'informatique': 'informatique',
}

@chatbot_bp.route('/')
@login_required
def index():
    # Get FAQ for display
    faqs = ChatbotFAQ.query.filter_by(language='fr').order_by(ChatbotFAQ.order).all()
    
    # Initialize FAQ if empty
    if not faqs:
        init_default_faqs()
        faqs = ChatbotFAQ.query.filter_by(language='fr').order_by(ChatbotFAQ.order).all()
    
    return render_template('chatbot/index.html', faqs=faqs)

def init_default_faqs():
    """Initialize default FAQ entries"""
    default_faqs = [
        {
            'question': 'Comment puis-je trouver des exercices ?',
            'answer': 'Vous pouvez trouver des exercices en allant dans la section "Exercices" depuis votre tableau de bord. Utilisez les filtres pour chercher par matière, niveau scolaire ou difficulté.',
            'keywords': 'exercice,trouver,chercher,recherche',
            'category': 'navigation',
            'order': 1
        },
        {
            'question': 'Comment télécharger un exercice ?',
            'answer': 'Pour télécharger un exercice : 1) Ouvrez l\'exercice souhaité, 2) Cliquez sur le bouton "Télécharger" situé en bas de la page.',
            'keywords': 'télécharger,download,fichier',
            'category': 'exercises',
            'order': 2
        },
        {
            'question': 'Comment poser une question sur un exercice ?',
            'answer': 'En bas de chaque exercice, vous trouverez une section "Questions". Cliquez sur "Poser une question" et entrez votre question. L\'enseignant ou d\'autres élèves pourront y répondre.',
            'keywords': 'question,poser,demander,aide',
            'category': 'exercises',
            'order': 3
        },
        {
            'question': 'Comment devenir enseignant sur la plateforme ?',
            'answer': 'Lors de l\'inscription, choisissez le rôle "Enseignant". Votre compte sera vérifié par un administrateur avant que vous puissiez publier des exercices.',
            'keywords': 'enseignant,teacher,professeur,inscrire',
            'category': 'account',
            'order': 4
        },
        {
            'question': 'Comment accéder aux corrigés ?',
            'answer': 'Si un corrigé est disponible pour un exercice, vous le trouverez dans la section "Corrigé" de la page de l\'exercice. Certains exercices n\'ont pas encore de corrigé.',
            'keywords': 'corrigé,correction,solution,réponse',
            'category': 'exercises',
            'order': 5
        },
        {
            'question': 'Comment utiliser le forum ?',
            'answer': 'Le forum est accessible depuis le menu principal. Vous pouvez y poser des questions, répondre aux autres élèves et participer aux discussions par matière.',
            'keywords': 'forum,discussion,communauté',
            'category': 'forum',
            'order': 6
        },
        {
            'question': 'Comment changer mon mot de passe ?',
            'answer': 'Allez dans "Mon profil" depuis le menu utilisateur, puis entrez votre nouveau mot de passe dans les champs prévus et cliquez sur "Enregistrer".',
            'keywords': 'mot de passe,password,changer,modifier',
            'category': 'account',
            'order': 7
        },
        {
            'question': 'Comment changer la langue du site ?',
            'answer': 'Cliquez sur le sélecteur de langue en haut de la page pour choisir entre Français, Kirundi et Anglais.',
            'keywords': 'langue,language,français,kirundi,anglais',
            'category': 'settings',
            'order': 8
        }
    ]
    
    for faq_data in default_faqs:
        faq = ChatbotFAQ(**faq_data)
        db.session.add(faq)
    
    db.session.commit()

@chatbot_bp.route('/ask', methods=['POST'])
@login_required
def ask():
    data = request.get_json()
    message = data.get('message', '').lower().strip()
    
    if not message:
        return jsonify({'response': 'Veuillez entrer une question.'})
    
    response = process_message(message)
    return jsonify({'response': response})

def process_message(message):
    """Process user message and return appropriate response"""
    
    # Check for exact matches in predefined responses
    for key, response in CHATBOT_RESPONSES.items():
        if key in message:
            return response
    
    # Check for subject-related queries
    for keyword, subject_code in SUBJECT_SUGGESTIONS.items():
        if keyword in message:
            return suggest_exercises_for_subject(subject_code)
    
    # Check for level-related queries
    for level_code, level_name in CLASS_LEVELS:
        if level_code.replace('eme', 'ème') in message or level_name.lower() in message:
            return suggest_exercises_for_level(level_code)
    
    # Search in FAQ database
    faq_response = search_faq(message)
    if faq_response:
        return faq_response
    
    # Default response
    return get_default_response()

def suggest_exercises_for_subject(subject_code):
    """Suggest exercises for a specific subject"""
    subject_name = subject_code
    for code, name in SUBJECTS:
        if code == subject_code:
            subject_name = name
            break
    
    exercises = Exercise.query.filter_by(
        subject=subject_code,
        is_published=True
    ).order_by(Exercise.created_at.desc()).limit(5).all()
    
    if exercises:
        response = f"Voici les derniers exercices en {subject_name} :\n\n"
        for i, ex in enumerate(exercises, 1):
            response += f"{i}. {ex.title} ({ex.get_level_name()})\n"
        response += f"\nVoulez-vous voir tous les exercices de {subject_name} ?"
    else:
        response = f"Il n'y a pas encore d'exercices en {subject_name}. Consultez d'autres matières ou revenez plus tard."
    
    return response

def suggest_exercises_for_level(level_code):
    """Suggest exercises for a specific class level"""
    level_name = level_code
    for code, name in CLASS_LEVELS:
        if code == level_code:
            level_name = name
            break
    
    exercises = Exercise.query.filter_by(
        class_level=level_code,
        is_published=True
    ).order_by(Exercise.created_at.desc()).limit(5).all()
    
    if exercises:
        response = f"Voici les derniers exercices pour la {level_name} :\n\n"
        for i, ex in enumerate(exercises, 1):
            response += f"{i}. {ex.title} ({ex.get_subject_name()})\n"
        response += f"\nVoulez-vous voir tous les exercices de ce niveau ?"
    else:
        response = f"Il n'y a pas encore d'exercices pour la {level_name}. Consultez d'autres niveaux ou revenez plus tard."
    
    return response

def search_faq(message):
    """Search FAQ database for matching answer"""
    faqs = ChatbotFAQ.query.all()
    
    for faq in faqs:
        # Check keywords
        if faq.keywords:
            keywords = faq.keywords.split(',')
            for keyword in keywords:
                if keyword.strip().lower() in message:
                    return faq.answer
        
        # Check question similarity (simple word matching)
        question_words = set(faq.question.lower().split())
        message_words = set(message.split())
        common_words = question_words.intersection(message_words)
        
        if len(common_words) >= 2:
            return faq.answer
    
    return None

def get_default_response():
    """Return default response when no match is found"""
    return """Je ne suis pas sûr de comprendre votre question. Voici ce que je peux vous aider à faire :

• Trouver des exercices par matière
• Naviguer sur le site
• Répondre aux questions fréquentes
• Expliquer comment utiliser le forum

Essayez de reformuler votre question ou tapez "aide" pour plus d'options."""

@chatbot_bp.route('/suggestions')
@login_required
def get_suggestions():
    """Get exercise suggestions based on user's level"""
    suggestions = []
    
    if current_user.class_level:
        exercises = Exercise.query.filter_by(
            class_level=current_user.class_level,
            is_published=True
        ).order_by(Exercise.view_count.desc()).limit(5).all()
        
        suggestions = [{
            'id': ex.id,
            'title': ex.title,
            'subject': ex.get_subject_name(),
            'difficulty': ex.difficulty
        } for ex in exercises]
    
    return jsonify({'suggestions': suggestions})
