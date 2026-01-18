from flask import Blueprint, render_template, redirect, url_for, flash, request, send_from_directory, current_app
from flask_login import login_required, current_user
from app import db
from app.models import Exercise, Question, Answer, SUBJECTS, CLASS_LEVELS
import os

student_bp = Blueprint('student', __name__)

@student_bp.route('/dashboard')
@login_required
def dashboard():
    # Get recommended exercises based on student's level
    recommended = []
    if current_user.class_level:
        recommended = Exercise.query.filter_by(
            class_level=current_user.class_level,
            is_published=True
        ).order_by(Exercise.created_at.desc()).limit(6).all()
    
    # Get latest exercises
    latest = Exercise.query.filter_by(is_published=True)\
        .order_by(Exercise.created_at.desc()).limit(6).all()
    
    # Get student's recent questions
    my_questions = Question.query.filter_by(author_id=current_user.id)\
        .order_by(Question.created_at.desc()).limit(5).all()
    
    return render_template('student/dashboard.html',
                         recommended=recommended,
                         latest=latest,
                         my_questions=my_questions,
                         subjects=SUBJECTS)

@student_bp.route('/exercices')
@login_required
def exercises():
    page = request.args.get('page', 1, type=int)
    subject = request.args.get('subject', '')
    level = request.args.get('level', '')
    difficulty = request.args.get('difficulty', '')
    search = request.args.get('search', '')
    
    query = Exercise.query.filter_by(is_published=True)
    
    if subject:
        query = query.filter_by(subject=subject)
    if level:
        query = query.filter_by(class_level=level)
    if difficulty:
        query = query.filter_by(difficulty=difficulty)
    if search:
        query = query.filter(
            db.or_(
                Exercise.title.ilike(f'%{search}%'),
                Exercise.description.ilike(f'%{search}%'),
                Exercise.theme.ilike(f'%{search}%')
            )
        )
    
    exercises = query.order_by(Exercise.created_at.desc())\
        .paginate(page=page, per_page=current_app.config['EXERCISES_PER_PAGE'])
    
    return render_template('student/exercises.html',
                         exercises=exercises,
                         subjects=SUBJECTS,
                         class_levels=CLASS_LEVELS,
                         current_subject=subject,
                         current_level=level,
                         current_difficulty=difficulty,
                         search=search)

@student_bp.route('/exercice/<int:id>')
@login_required
def view_exercise(id):
    exercise = Exercise.query.get_or_404(id)
    
    if not exercise.is_published:
        flash('Cet exercice n\'est pas disponible.', 'warning')
        return redirect(url_for('student.exercises'))
    
    # Increment view count
    exercise.view_count += 1
    db.session.commit()
    
    # Get questions for this exercise
    questions = exercise.questions.order_by(Question.created_at.desc()).all()
    
    return render_template('student/view_exercise.html',
                         exercise=exercise,
                         questions=questions)

@student_bp.route('/exercice/<int:id>/download')
@login_required
def download_exercise(id):
    exercise = Exercise.query.get_or_404(id)
    
    if not exercise.file_path:
        flash('Aucun fichier disponible pour cet exercice.', 'warning')
        return redirect(url_for('student.view_exercise', id=id))
    
    # Increment download count
    exercise.download_count += 1
    db.session.commit()
    
    # Get the directory and filename
    directory = os.path.join(current_app.root_path, 'static')
    return send_from_directory(directory, exercise.file_path, as_attachment=True)

@student_bp.route('/exercice/<int:id>/download-correction')
@login_required
def download_correction(id):
    exercise = Exercise.query.get_or_404(id)
    
    if not exercise.correction_file_path:
        flash('Aucun fichier de correction disponible.', 'warning')
        return redirect(url_for('student.view_exercise', id=id))
    
    directory = os.path.join(current_app.root_path, 'static')
    return send_from_directory(directory, exercise.correction_file_path, as_attachment=True)

@student_bp.route('/exercice/<int:id>/question', methods=['POST'])
@login_required
def ask_question(id):
    exercise = Exercise.query.get_or_404(id)
    content = request.form.get('content')
    
    if content:
        question = Question(
            content=content,
            author_id=current_user.id,
            exercise_id=exercise.id
        )
        db.session.add(question)
        db.session.commit()
        flash('Votre question a été posée avec succès.', 'success')
    else:
        flash('Veuillez entrer une question.', 'warning')
    
    return redirect(url_for('student.view_exercise', id=id))

@student_bp.route('/question/<int:id>/repondre', methods=['POST'])
@login_required
def answer_question(id):
    question = Question.query.get_or_404(id)
    content = request.form.get('content')
    
    if content:
        answer = Answer(
            content=content,
            author_id=current_user.id,
            question_id=question.id
        )
        db.session.add(answer)
        db.session.commit()
        flash('Votre réponse a été envoyée.', 'success')
    
    return redirect(url_for('student.view_exercise', id=question.exercise_id))

@student_bp.route('/mes-questions')
@login_required
def my_questions():
    questions = Question.query.filter_by(author_id=current_user.id)\
        .order_by(Question.created_at.desc()).all()
    return render_template('student/my_questions.html', questions=questions)

@student_bp.route('/matiere/<subject>')
@login_required
def subject_exercises(subject):
    page = request.args.get('page', 1, type=int)
    level = request.args.get('level', '')
    
    query = Exercise.query.filter_by(subject=subject, is_published=True)
    
    if level:
        query = query.filter_by(class_level=level)
    
    exercises = query.order_by(Exercise.created_at.desc())\
        .paginate(page=page, per_page=current_app.config['EXERCISES_PER_PAGE'])
    
    # Get subject name
    subject_name = subject
    for code, name in SUBJECTS:
        if code == subject:
            subject_name = name
            break
    
    return render_template('student/subject_exercises.html',
                         exercises=exercises,
                         subject=subject,
                         subject_name=subject_name,
                         class_levels=CLASS_LEVELS,
                         current_level=level)
