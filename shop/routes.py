from shop import app, db, bcrypt
from flask import redirect, url_for, flash, render_template, request
from .models import *
from .forms import *

from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
@app.route('/home/')
def home_page():
    return render_template('index.html', title='Home')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data, username=form.username.data, email=form.email.data, password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Welcome, {form.name.data}Thanks for registering!', 'success')
        return redirect(url_for('home_page'))

    return render_template('components/register.html', form=form)
