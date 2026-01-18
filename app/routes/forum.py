from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_required, current_user
from app import db
from app.models import ForumCategory, ForumPost, ForumReply, SUBJECTS, CLASS_LEVELS

forum_bp = Blueprint('forum', __name__)

@forum_bp.route('/')
@login_required
def index():
    categories = ForumCategory.query.order_by(ForumCategory.order).all()
    
    # If no categories exist, create default ones
    if not categories:
        create_default_categories()
        categories = ForumCategory.query.order_by(ForumCategory.order).all()
    
    # Recent posts
    recent_posts = ForumPost.query.order_by(ForumPost.created_at.desc()).limit(5).all()
    
    return render_template('forum/index.html',
                         categories=categories,
                         recent_posts=recent_posts)

def create_default_categories():
    """Create default forum categories"""
    default_categories = [
        {
            'name': 'Discussions Générales',
            'description': 'Discussions sur l\'éducation et sujets divers',
            'slug': 'general',
            'icon': 'fas fa-comments',
            'order': 1
        },
        {
            'name': 'Aide aux devoirs',
            'description': 'Demandez de l\'aide pour vos devoirs',
            'slug': 'aide-devoirs',
            'icon': 'fas fa-book-open',
            'order': 2
        },
        {
            'name': 'Mathématiques',
            'description': 'Questions et discussions sur les mathématiques',
            'slug': 'mathematiques',
            'subject': 'mathematiques',
            'icon': 'fas fa-calculator',
            'order': 3
        },
        {
            'name': 'Sciences (Physique, Chimie, Biologie)',
            'description': 'Questions sur les sciences',
            'slug': 'sciences',
            'icon': 'fas fa-flask',
            'order': 4
        },
        {
            'name': 'Langues (Français, Anglais, Kirundi)',
            'description': 'Questions sur les langues',
            'slug': 'langues',
            'icon': 'fas fa-language',
            'order': 5
        },
        {
            'name': 'Sciences Humaines',
            'description': 'Histoire, Géographie, Économie, Philosophie',
            'slug': 'sciences-humaines',
            'icon': 'fas fa-globe',
            'order': 6
        },
        {
            'name': 'Préparation aux examens',
            'description': 'Conseils et ressources pour les examens',
            'slug': 'examens',
            'icon': 'fas fa-graduation-cap',
            'order': 7
        },
        {
            'name': 'Orientation scolaire',
            'description': 'Questions sur l\'orientation et les études',
            'slug': 'orientation',
            'icon': 'fas fa-compass',
            'order': 8
        }
    ]
    
    for cat_data in default_categories:
        category = ForumCategory(**cat_data)
        db.session.add(category)
    
    db.session.commit()

@forum_bp.route('/categorie/<slug>')
@login_required
def category(slug):
    category = ForumCategory.query.filter_by(slug=slug).first_or_404()
    page = request.args.get('page', 1, type=int)
    
    posts = category.posts.order_by(
        ForumPost.is_pinned.desc(),
        ForumPost.created_at.desc()
    ).paginate(page=page, per_page=current_app.config['POSTS_PER_PAGE'])
    
    return render_template('forum/category.html',
                         category=category,
                         posts=posts)

@forum_bp.route('/categorie/<slug>/nouveau', methods=['GET', 'POST'])
@login_required
def new_post(slug):
    category = ForumCategory.query.filter_by(slug=slug).first_or_404()
    
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        
        if not title or not content:
            flash('Veuillez remplir tous les champs.', 'warning')
            return redirect(url_for('forum.new_post', slug=slug))
        
        post = ForumPost(
            title=title,
            content=content,
            author_id=current_user.id,
            category_id=category.id
        )
        db.session.add(post)
        db.session.commit()
        
        flash('Votre sujet a été créé avec succès.', 'success')
        return redirect(url_for('forum.view_post', id=post.id))
    
    return render_template('forum/new_post.html', category=category)

@forum_bp.route('/sujet/<int:id>')
@login_required
def view_post(id):
    post = ForumPost.query.get_or_404(id)
    post.view_count += 1
    db.session.commit()
    
    replies = post.replies.order_by(ForumReply.created_at.asc()).all()
    
    return render_template('forum/view_post.html',
                         post=post,
                         replies=replies)

@forum_bp.route('/sujet/<int:id>/repondre', methods=['POST'])
@login_required
def reply_post(id):
    post = ForumPost.query.get_or_404(id)
    
    if post.is_locked:
        flash('Ce sujet est verrouillé.', 'warning')
        return redirect(url_for('forum.view_post', id=id))
    
    content = request.form.get('content')
    
    if not content:
        flash('Veuillez entrer une réponse.', 'warning')
        return redirect(url_for('forum.view_post', id=id))
    
    reply = ForumReply(
        content=content,
        author_id=current_user.id,
        post_id=post.id
    )
    db.session.add(reply)
    db.session.commit()
    
    flash('Votre réponse a été ajoutée.', 'success')
    return redirect(url_for('forum.view_post', id=id))

@forum_bp.route('/sujet/<int:id>/pin', methods=['POST'])
@login_required
def pin_post(id):
    if not current_user.is_teacher() and not current_user.is_admin():
        flash('Action non autorisée.', 'danger')
        return redirect(url_for('forum.view_post', id=id))
    
    post = ForumPost.query.get_or_404(id)
    post.is_pinned = not post.is_pinned
    db.session.commit()
    
    status = 'épinglé' if post.is_pinned else 'désépinglé'
    flash(f'Sujet {status}.', 'success')
    return redirect(url_for('forum.view_post', id=id))

@forum_bp.route('/sujet/<int:id>/lock', methods=['POST'])
@login_required
def lock_post(id):
    if not current_user.is_teacher() and not current_user.is_admin():
        flash('Action non autorisée.', 'danger')
        return redirect(url_for('forum.view_post', id=id))
    
    post = ForumPost.query.get_or_404(id)
    post.is_locked = not post.is_locked
    db.session.commit()
    
    status = 'verrouillé' if post.is_locked else 'déverrouillé'
    flash(f'Sujet {status}.', 'success')
    return redirect(url_for('forum.view_post', id=id))

@forum_bp.route('/reponse/<int:id>/solution', methods=['POST'])
@login_required
def mark_solution(id):
    reply = ForumReply.query.get_or_404(id)
    post = reply.post
    
    # Only post author or teachers can mark solution
    if current_user.id != post.author_id and not current_user.is_teacher():
        flash('Action non autorisée.', 'danger')
        return redirect(url_for('forum.view_post', id=post.id))
    
    # Unmark other solutions
    ForumReply.query.filter_by(post_id=post.id).update({'is_solution': False})
    
    reply.is_solution = True
    db.session.commit()
    
    flash('Réponse marquée comme solution.', 'success')
    return redirect(url_for('forum.view_post', id=post.id))

@forum_bp.route('/recherche')
@login_required
def search():
    query = request.args.get('q', '')
    page = request.args.get('page', 1, type=int)
    
    if query:
        posts = ForumPost.query.filter(
            db.or_(
                ForumPost.title.ilike(f'%{query}%'),
                ForumPost.content.ilike(f'%{query}%')
            )
        ).order_by(ForumPost.created_at.desc())\
            .paginate(page=page, per_page=current_app.config['POSTS_PER_PAGE'])
    else:
        posts = None
    
    return render_template('forum/search.html',
                         query=query,
                         posts=posts)
