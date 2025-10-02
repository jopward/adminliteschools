# apps/authentication/__init__.py
from flask import Blueprint

# تعريف الـ Blueprint
blueprint = Blueprint(
    'authentication_blueprint',   # اسم الـ Blueprint
    __name__,
    template_folder='templates',  # مكان ملفات القوالب
    url_prefix='/auth'            # كل الراوتات تحت /auth
)
