from flask import render_template, flash, redirect, url_for, request
from . import auth
from .forms import EmailPasswordForm
from ..models import User
from flask_login import login_user, login_required, logout_user

@auth.route('/login', methods=["GET", "POST"])
def login():
    form = EmailPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.verify_password(form.password.data):
            flash('Please check your credentials!', 'error')
            return redirect(url_for('.login'))

        login_user(user, form.remember_me.data)
        flash('Successfully logged in!', 'success')
        return redirect(request.args.get('next') or url_for('main.dashboard'))
    return render_template("login.html", form = form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out!', 'success')
    return redirect(url_for('.login'))
