from flask import Blueprint, render_template, redirect, url_for, session

school_bp = Blueprint('school', __name__, template_folder='../templates')

@school_bp.route('/')
def home():
    return render_template('schools/index.html')

@school_bp.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('user'):
        return redirect(url_for('school.home'))
    return render_template('schools/login.html')
