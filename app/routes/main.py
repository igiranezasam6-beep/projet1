from flask import Blueprint, render_template, session, redirect, url_for
from flask_login import current_user
from app.models import Exercise, ForumPost, SUBJECTS, CLASS_LEVELS

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    # Get latest exercises
    latest_exercises = Exercise.query.filter_by(is_published=True)\
        .order_by(Exercise.created_at.desc()).limit(6).all()
    
    # Get popular exercises
    popular_exercises = Exercise.query.filter_by(is_published=True)\
        .order_by(Exercise.view_count.desc()).limit(6).all()
    
    # Get latest forum posts
    latest_posts = ForumPost.query.order_by(ForumPost.created_at.desc()).limit(5).all()
    
    # Statistics
    total_exercises = Exercise.query.filter_by(is_published=True).count()
    
    return render_template('index.html',
                         latest_exercises=latest_exercises,
                         popular_exercises=popular_exercises,
                         latest_posts=latest_posts,
                         total_exercises=total_exercises,
                         subjects=SUBJECTS,
                         class_levels=CLASS_LEVELS)

@main_bp.route('/set-language/<lang>')
def set_language(lang):
    if lang in ['fr', 'rn', 'en']:
        session['language'] = lang
        if current_user.is_authenticated:
            current_user.language = lang
            from app import db
            db.session.commit()
    return redirect(url_for('main.index'))

@main_bp.route('/about')
def about():
    return render_template('about.html')

@main_bp.route('/contact')
def contact():
    return render_template('contact.html')
