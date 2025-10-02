# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import os
from sys import exit
from flask_migrate import Migrate
from flask_minify import Minify
from apps import create_app, db
from apps.config import config_dict
from apps.schools import init_app as init_schools   # 👈 بس هذا نستدعيه

# DEBUG
DEBUG = (os.getenv('DEBUG', 'False') == 'True')

# اختيار الإعدادات
get_config_mode = 'Debug' if DEBUG else 'Production'
try:
    app_config = config_dict[get_config_mode.capitalize()]
except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')

# إنشاء التطبيق
app = create_app(app_config)

# ✅ سجل قسم المدارس فقط من هنا
init_schools(app)

# إنشاء الجداول & fallback إلى SQLite إذا فشل
with app.app_context():
    try:
        db.create_all()  # إنشاء الجداول
    except Exception as e:
        print('> Error: DBMS Exception: ' + str(e))
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
        print('> Fallback to SQLite ')
        db.create_all()

# Apply all changes
Migrate(app, db)

# Minify إذا لم يكن DEBUG
if not DEBUG:
    Minify(app=app, html=True, js=False, cssless=False)

# Logging
if DEBUG:
    app.logger.info('DEBUG            = ' + str(DEBUG))
    app.logger.info('Page Compression = ' + ('FALSE' if DEBUG else 'TRUE'))
    app.logger.info('DBMS             = ' + app_config.SQLALCHEMY_DATABASE_URI)

# تشغيل التطبيق
if __name__ == "__main__":
    app.run(debug=DEBUG)
