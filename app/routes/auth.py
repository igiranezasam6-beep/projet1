from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from urllib.parse import urlparse
from app import db
from app.models import User, CLASS_LEVELS

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = request.form.get('remember', False)
        
        user = User.query.filter_by(email=email).first()
        
        if user is None or not user.check_password(password):
            flash('Email ou mot de passe incorrect.', 'danger')
            return redirect(url_for('auth.login'))
        
        login_user(user, remember=remember)
        user.last_seen = db.func.now()
        db.session.commit()
        
        next_page = request.args.get('next')
        if not next_page or urlparse(next_page).netloc != '':
            if user.is_teacher():
                next_page = url_for('teacher.dashboard')
            else:
                next_page = url_for('student.dashboard')
        
        flash(f'Bienvenue, {user.get_full_name()}!', 'success')
        return redirect(next_page)
    
    return render_template('auth/login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        role = request.form.get('role', 'student')
        class_level = request.form.get('class_level')
        school = request.form.get('school')
        
        # Validation
        if password != confirm_password:
            flash('Les mots de passe ne correspondent pas.', 'danger')
            return redirect(url_for('auth.register'))
        
        if User.query.filter_by(username=username).first():
            flash('Ce nom d\'utilisateur est déjà pris.', 'danger')
            return redirect(url_for('auth.register'))
        
        if User.query.filter_by(email=email).first():
            flash('Cet email est déjà utilisé.', 'danger')
            return redirect(url_for('auth.register'))
        
        # Create user
        user = User(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            role=role,
            class_level=class_level if role == 'student' else None,
            school=school,
            is_verified=True if role == 'student' else False  # Teachers need verification
        )
        user.set_password(password)
        
        db.session.add(user)
        db.session.commit()
        
        if role == 'teacher':
            flash('Votre compte enseignant a été créé. Il sera vérifié par un administrateur.', 'info')
        else:
            flash('Votre compte a été créé avec succès! Vous pouvez maintenant vous connecter.', 'success')
        
        return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html', class_levels=CLASS_LEVELS)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Vous avez été déconnecté.', 'info')
    return redirect(url_for('main.index'))

@auth_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        current_user.first_name = request.form.get('first_name')
        current_user.last_name = request.form.get('last_name')
        current_user.school = request.form.get('school')
        
        if current_user.role == 'student':
            current_user.class_level = request.form.get('class_level')
        
        # Change password if provided
        new_password = request.form.get('new_password')
        if new_password:
            confirm_password = request.form.get('confirm_password')
            if new_password == confirm_password:
                current_user.set_password(new_password)
                flash('Mot de passe mis à jour.', 'success')
            else:
                flash('Les mots de passe ne correspondent pas.', 'danger')
        
        db.session.commit()
        flash('Profil mis à jour avec succès.', 'success')
        return redirect(url_for('auth.profile'))
    
    return render_template('auth/profile.html', class_levels=CLASS_LEVELS)
