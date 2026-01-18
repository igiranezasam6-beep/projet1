from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login_manager

# Association tables
exercise_views = db.Table('exercise_views',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('exercise_id', db.Integer, db.ForeignKey('exercise.id'), primary_key=True),
    db.Column('viewed_at', db.DateTime, default=datetime.utcnow)
)

# Subjects (Matières)
SUBJECTS = [
    ('mathematiques', 'Mathématiques'),
    ('physique', 'Physique'),
    ('chimie', 'Chimie'),
    ('biologie', 'Biologie'),
    ('francais', 'Français'),
    ('anglais', 'Anglais'),
    ('kirundi', 'Kirundi'),
    ('histoire', 'Histoire'),
    ('geographie', 'Géographie'),
    ('economie', 'Économie'),
    ('philosophie', 'Philosophie'),
    ('informatique', 'Informatique'),
    ('education_civique', 'Éducation Civique'),
    ('sciences_sociales', 'Sciences Sociales')
]

# Class levels (Niveaux)
CLASS_LEVELS = [
    ('7eme', '7ème année'),
    ('8eme', '8ème année'),
    ('9eme', '9ème année'),
    ('10eme', '10ème année (1ère)'),
    ('11eme', '11ème année (2ème)'),
    ('12eme', '12ème année (3ème)'),
    ('13eme', '13ème année (Terminale)')
]

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256))
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    role = db.Column(db.String(20), default='student')  # 'student', 'teacher', 'admin'
    is_verified = db.Column(db.Boolean, default=False)
    language = db.Column(db.String(5), default='fr')
    class_level = db.Column(db.String(20))  # For students
    school = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    exercises = db.relationship('Exercise', backref='author', lazy='dynamic')
    questions = db.relationship('Question', backref='author', lazy='dynamic')
    answers = db.relationship('Answer', backref='author', lazy='dynamic')
    forum_posts = db.relationship('ForumPost', backref='author', lazy='dynamic')
    forum_replies = db.relationship('ForumReply', backref='author', lazy='dynamic')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username
    
    def is_teacher(self):
        return self.role == 'teacher'
    
    def is_admin(self):
        return self.role == 'admin'
    
    def __repr__(self):
        return f'<User {self.username}>'


class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    subject = db.Column(db.String(50), nullable=False, index=True)
    class_level = db.Column(db.String(20), nullable=False, index=True)
    theme = db.Column(db.String(100))
    difficulty = db.Column(db.String(20), default='moyen')  # 'facile', 'moyen', 'difficile'
    file_path = db.Column(db.String(256))
    content = db.Column(db.Text)  # For text-based exercises
    video_url = db.Column(db.String(256))  # YouTube or other video link
    has_correction = db.Column(db.Boolean, default=False)
    correction_file_path = db.Column(db.String(256))
    correction_content = db.Column(db.Text)
    view_count = db.Column(db.Integer, default=0)
    download_count = db.Column(db.Integer, default=0)
    is_published = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Foreign keys
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # Relationships
    questions = db.relationship('Question', backref='exercise', lazy='dynamic', cascade='all, delete-orphan')
    
    def get_subject_name(self):
        for code, name in SUBJECTS:
            if code == self.subject:
                return name
        return self.subject
    
    def get_level_name(self):
        for code, name in CLASS_LEVELS:
            if code == self.class_level:
                return name
        return self.class_level
    
    def __repr__(self):
        return f'<Exercise {self.title}>'


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_resolved = db.Column(db.Boolean, default=False)
    
    # Foreign keys
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'), nullable=False)
    
    # Relationships
    answers = db.relationship('Answer', backref='question', lazy='dynamic', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Question {self.id}>'


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    is_accepted = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Foreign keys
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    
    def __repr__(self):
        return f'<Answer {self.id}>'


class ForumCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(256))
    slug = db.Column(db.String(100), unique=True, nullable=False)
    subject = db.Column(db.String(50))  # Optional: link to a subject
    class_level = db.Column(db.String(20))  # Optional: link to a level
    icon = db.Column(db.String(50), default='fas fa-comments')
    order = db.Column(db.Integer, default=0)
    
    # Relationships
    posts = db.relationship('ForumPost', backref='category', lazy='dynamic')
    
    def post_count(self):
        return self.posts.count()
    
    def __repr__(self):
        return f'<ForumCategory {self.name}>'


class ForumPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    is_pinned = db.Column(db.Boolean, default=False)
    is_locked = db.Column(db.Boolean, default=False)
    view_count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Foreign keys
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('forum_category.id'), nullable=False)
    
    # Relationships
    replies = db.relationship('ForumReply', backref='post', lazy='dynamic', cascade='all, delete-orphan')
    
    def reply_count(self):
        return self.replies.count()
    
    def last_activity(self):
        last_reply = self.replies.order_by(ForumReply.created_at.desc()).first()
        if last_reply:
            return last_reply.created_at
        return self.created_at
    
    def __repr__(self):
        return f'<ForumPost {self.title}>'


class ForumReply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    is_solution = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Foreign keys
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('forum_post.id'), nullable=False)
    
    def __repr__(self):
        return f'<ForumReply {self.id}>'


class ChatbotFAQ(db.Model):
    """Frequently asked questions for the chatbot"""
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(256), nullable=False)
    answer = db.Column(db.Text, nullable=False)
    keywords = db.Column(db.String(256))  # Comma-separated keywords
    category = db.Column(db.String(50), default='general')
    language = db.Column(db.String(5), default='fr')
    order = db.Column(db.Integer, default=0)
    
    def __repr__(self):
        return f'<ChatbotFAQ {self.question[:50]}>'
