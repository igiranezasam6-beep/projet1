import os
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from app import db
from app.models import Exercise, Question, Answer, SUBJECTS, CLASS_LEVELS
from functools import wraps

teacher_bp = Blueprint('teacher', __name__)

def teacher_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_teacher():
            flash('Accès réservé aux enseignants.', 'danger')
            return redirect(url_for('main.index'))
        if not current_user.is_verified:
            flash('Votre compte enseignant n\'a pas encore été vérifié.', 'warning')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

@teacher_bp.route('/dashboard')
@login_required
@teacher_required
def dashboard():
    # Get teacher's exercises
    exercises = Exercise.query.filter_by(author_id=current_user.id)\
        .order_by(Exercise.created_at.desc()).all()
    
    # Statistics
    total_exercises = len(exercises)
    total_views = sum(e.view_count for e in exercises)
    total_downloads = sum(e.download_count for e in exercises)
    
    # Recent questions on teacher's exercises
    recent_questions = Question.query.join(Exercise)\
        .filter(Exercise.author_id == current_user.id)\
        .order_by(Question.created_at.desc()).limit(5).all()
    
    return render_template('teacher/dashboard.html',
                         exercises=exercises,
                         total_exercises=total_exercises,
                         total_views=total_views,
                         total_downloads=total_downloads,
                         recent_questions=recent_questions)

@teacher_bp.route('/exercice/nouveau', methods=['GET', 'POST'])
@login_required
@teacher_required
def new_exercise():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        subject = request.form.get('subject')
        class_level = request.form.get('class_level')
        theme = request.form.get('theme')
        difficulty = request.form.get('difficulty', 'moyen')
        content = request.form.get('content')
        video_url = request.form.get('video_url')
        
        # Create exercise
        exercise = Exercise(
            title=title,
            description=description,
            subject=subject,
            class_level=class_level,
            theme=theme,
            difficulty=difficulty,
            content=content,
            video_url=video_url,
            author_id=current_user.id
        )
        
        # Handle exercise file upload
        if 'exercise_file' in request.files:
            file = request.files['exercise_file']
            if file and file.filename and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                # Add timestamp to filename
                import time
                filename = f"{int(time.time())}_{filename}"
                file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], 'exercises', filename)
                file.save(file_path)
                exercise.file_path = f"uploads/exercises/{filename}"
        
        # Handle correction file upload
        if 'correction_file' in request.files:
            file = request.files['correction_file']
            if file and file.filename and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                import time
                filename = f"{int(time.time())}_{filename}"
                file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], 'corrections', filename)
                file.save(file_path)
                exercise.correction_file_path = f"uploads/corrections/{filename}"
                exercise.has_correction = True
        
        # Handle correction content
        correction_content = request.form.get('correction_content')
        if correction_content:
            exercise.correction_content = correction_content
            exercise.has_correction = True
        
        db.session.add(exercise)
        db.session.commit()
        
        flash('Exercice créé avec succès!', 'success')
        return redirect(url_for('teacher.dashboard'))
    
    return render_template('teacher/new_exercise.html',
                         subjects=SUBJECTS,
                         class_levels=CLASS_LEVELS)

@teacher_bp.route('/exercice/<int:id>/modifier', methods=['GET', 'POST'])
@login_required
@teacher_required
def edit_exercise(id):
    exercise = Exercise.query.get_or_404(id)
    
    if exercise.author_id != current_user.id:
        flash('Vous ne pouvez pas modifier cet exercice.', 'danger')
        return redirect(url_for('teacher.dashboard'))
    
    if request.method == 'POST':
        exercise.title = request.form.get('title')
        exercise.description = request.form.get('description')
        exercise.subject = request.form.get('subject')
        exercise.class_level = request.form.get('class_level')
        exercise.theme = request.form.get('theme')
        exercise.difficulty = request.form.get('difficulty', 'moyen')
        exercise.content = request.form.get('content')
        exercise.video_url = request.form.get('video_url')
        exercise.is_published = 'is_published' in request.form
        
        # Handle new exercise file upload
        if 'exercise_file' in request.files:
            file = request.files['exercise_file']
            if file and file.filename and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                import time
                filename = f"{int(time.time())}_{filename}"
                file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], 'exercises', filename)
                file.save(file_path)
                exercise.file_path = f"uploads/exercises/{filename}"
        
        # Handle new correction file upload
        if 'correction_file' in request.files:
            file = request.files['correction_file']
            if file and file.filename and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                import time
                filename = f"{int(time.time())}_{filename}"
                file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], 'corrections', filename)
                file.save(file_path)
                exercise.correction_file_path = f"uploads/corrections/{filename}"
                exercise.has_correction = True
        
        # Handle correction content
        correction_content = request.form.get('correction_content')
        if correction_content:
            exercise.correction_content = correction_content
            exercise.has_correction = True
        
        db.session.commit()
        flash('Exercice mis à jour avec succès!', 'success')
        return redirect(url_for('teacher.dashboard'))
    
    return render_template('teacher/edit_exercise.html',
                         exercise=exercise,
                         subjects=SUBJECTS,
                         class_levels=CLASS_LEVELS)

@teacher_bp.route('/exercice/<int:id>/supprimer', methods=['POST'])
@login_required
@teacher_required
def delete_exercise(id):
    exercise = Exercise.query.get_or_404(id)
    
    if exercise.author_id != current_user.id:
        flash('Vous ne pouvez pas supprimer cet exercice.', 'danger')
        return redirect(url_for('teacher.dashboard'))
    
    db.session.delete(exercise)
    db.session.commit()
    
    flash('Exercice supprimé avec succès.', 'success')
    return redirect(url_for('teacher.dashboard'))

@teacher_bp.route('/questions')
@login_required
@teacher_required
def questions():
    # Get all questions on teacher's exercises
    questions = Question.query.join(Exercise)\
        .filter(Exercise.author_id == current_user.id)\
        .order_by(Question.created_at.desc()).all()
    
    return render_template('teacher/questions.html', questions=questions)

@teacher_bp.route('/question/<int:id>/repondre', methods=['POST'])
@login_required
@teacher_required
def answer_question(id):
    question = Question.query.get_or_404(id)
    
    # Verify the question is on teacher's exercise
    if question.exercise.author_id != current_user.id:
        flash('Vous ne pouvez pas répondre à cette question.', 'danger')
        return redirect(url_for('teacher.questions'))
    
    content = request.form.get('content')
    if content:
        answer = Answer(
            content=content,
            author_id=current_user.id,
            question_id=question.id,
            is_accepted=True  # Teacher's answer is automatically accepted
        )
        question.is_resolved = True
        db.session.add(answer)
        db.session.commit()
        flash('Réponse envoyée avec succès.', 'success')
    
    return redirect(url_for('teacher.questions'))

@teacher_bp.route('/statistiques')
@login_required
@teacher_required
def statistics():
    exercises = Exercise.query.filter_by(author_id=current_user.id).all()
    
    # Prepare statistics data
    stats_by_subject = {}
    stats_by_level = {}
    
    for exercise in exercises:
        # By subject
        subject_name = exercise.get_subject_name()
        if subject_name not in stats_by_subject:
            stats_by_subject[subject_name] = {'count': 0, 'views': 0, 'downloads': 0}
        stats_by_subject[subject_name]['count'] += 1
        stats_by_subject[subject_name]['views'] += exercise.view_count
        stats_by_subject[subject_name]['downloads'] += exercise.download_count
        
        # By level
        level_name = exercise.get_level_name()
        if level_name not in stats_by_level:
            stats_by_level[level_name] = {'count': 0, 'views': 0, 'downloads': 0}
        stats_by_level[level_name]['count'] += 1
        stats_by_level[level_name]['views'] += exercise.view_count
        stats_by_level[level_name]['downloads'] += exercise.download_count
    
    return render_template('teacher/statistics.html',
                         exercises=exercises,
                         stats_by_subject=stats_by_subject,
                         stats_by_level=stats_by_level)
