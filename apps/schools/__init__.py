# -*- encoding: utf-8 -*-
"""
apps/schools/__init__.py
تهيئة قسم المدارس في مشروع AdminLTE Flask
"""
from flask import Blueprint, Flask
from importlib import import_module
from apps.schools.school_auth import school_auth_bp

# --- Blueprint رئيسي لقسم المدارس ---
schools_bp = Blueprint(
    'schools_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)

# --- تسجيل جميع الروتس الموجودة داخل المجلد routes ---
def register_school_routes(app: Flask):
    route_modules = ['attendance', 'teachers', 'students']
    for module_name in route_modules:
        module = import_module(f'apps.schools.routes.{module_name}')
        if hasattr(module, f'{module_name}_bp'):
            app.register_blueprint(getattr(module, f'{module_name}_bp'))

# --- دالة لإنشاء الجداول ---
def init_db():
    from apps.schools.db.db_setup import create_tables, seed_superadmin
    create_tables()
    seed_superadmin()

# --- تهيئة القسم مع التطبيق الرئيسي ---
def init_app(app: Flask):
    # تسجيل الـ Blueprint الرئيسي
    app.register_blueprint(schools_bp, url_prefix='/schools')

    # تسجيل الروتس الفرعية
    register_school_routes(app)

    # تسجيل الأوث
    app.register_blueprint(school_auth_bp, url_prefix='/schools/auth')

    # إنشاء الجداول إذا لم تكن موجودة
    init_db()
