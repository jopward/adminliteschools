# -*- encoding: utf-8 -*-
"""
__init__.py for routes package
"""

# استيراد جميع Blueprints من ملفات routes حسب الأسماء الصحيحة
from .attendance import attendance_bp
from .classes import classes_bp
from .students import student_bp
from .teachers import teacher_bp
from .subjects import subjects_bp
from .grades import grades_bp
from .school import school_bp
from .school_routes import school_bp as school_routes_bp   # تم التأكد من الاسم الصحيح
from .auth import auth_bp
from .tracking import tracking_bp
from .class_subjects import class_subjects_bp
from .user import user_bp

# دالة لتسجيل كل Blueprints في التطبيق
def register_blueprints(app):
    app.register_blueprint(attendance_bp, url_prefix='/attendance')
    app.register_blueprint(classes_bp, url_prefix='/classes')
    app.register_blueprint(student_bp, url_prefix='/students')
    app.register_blueprint(teacher_bp, url_prefix='/teachers')
    app.register_blueprint(subjects_bp, url_prefix='/subjects')
    app.register_blueprint(grades_bp, url_prefix='/grades')
    app.register_blueprint(school_bp, url_prefix='/school')
    app.register_blueprint(school_routes_bp, url_prefix='/school_routes')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(tracking_bp, url_prefix='/tracking')
    app.register_blueprint(class_subjects_bp, url_prefix='/class_subjects')
    app.register_blueprint(user_bp, url_prefix='/user')
