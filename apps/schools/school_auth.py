from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from functools import wraps
from apps.schools.models.user import verify_user, get_user_by_id, create_user

school_auth_bp = Blueprint('school_auth', __name__, url_prefix='/auth')

# ----------------------------
# تسجيل مستخدم جديد
# ----------------------------
@school_auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')
        role = request.form.get('role')  # superadmin / admin / teacher
        school_id = request.form.get('school_id') or None

        try:
            user_id = create_user(name, username, password, role, school_id)
            flash("تم إنشاء الحساب بنجاح 🎉", "success")
            return redirect(url_for('school_auth.login'))
        except Exception as e:
            flash(f"❌ خطأ أثناء إنشاء الحساب: {e}", "danger")

    return render_template('register.html')


# ----------------------------
# صفحة تسجيل الدخول
# ----------------------------
@school_auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = verify_user(username, password)
        if user:
            session['user_id'] = user['id']
            session['role'] = user['role']
            flash("تم تسجيل الدخول بنجاح ✅", "success")
            return redirect(url_for('home'))  # عدّل 'home' حسب الراوت اللي عندك
        else:
            flash("❌ اسم المستخدم أو كلمة المرور غير صحيحة", "danger")

    return render_template('login.html')


# ----------------------------
# تسجيل الخروج
# ----------------------------
@school_auth_bp.route('/logout')
def logout():
    session.clear()
    flash("تم تسجيل الخروج 👋", "info")
    return redirect(url_for('school_auth.login'))


# ----------------------------
# ديكوريتر للتحقق من تسجيل الدخول
# ----------------------------
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("يجب تسجيل الدخول أولاً ⚠️", "warning")
            return redirect(url_for('school_auth.login'))
        return f(*args, **kwargs)
    return decorated_function
