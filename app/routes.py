######################
# AUTHENTICATION ROUTES
######################
# from flask import Flask, render_template, request, redirect, url_for, flash, abort

from app import app
# from app.forms import LoginForm, RegistrationForm, EditProfileForm, ResetPasswordRequestForm, ResetPasswordForm
# from app.email import send_email_password_reset
# from app.models import NetUser
#
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import migrate
# from flask_login import current_user, login_user, logout_user, login_required
# from werkzeug.urls import url_parse
# from datetime import datetime


@app.route('/')
def index():
    html = {}
    html['title']          = "Welcome back - Login"
    html['description']    = "Welcome back. Nice to see you."
    html['content']        = "This is a test!"
    return render_template('index.html', html=html)



##############################
# PUBLIC
##############################
# #registration page
# @app.route('/', methods=['GET', 'POST'])
# def register():
#
#     html = {}
#     html['title']          = "Register"
#     html['description']    = "Join us today"
#     html['content']        = ""
#
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#
#     form = RegistrationForm()
#
#     if form.validate_on_submit():
#         user = NetUser(email=form.email.data)
#         user.set_password(form.password1.data)
#         db.session.add(user)
#         db.session.commit()
#         flash("Welcome. You're now registered!")
#         return redirect(url_for('login'))
#
#     return render_template('register.html',
#                            html=html,
#                            form=form)
#
#
#
# #route for login
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#
#     html = {}
#     html['title']          = "Welcome back - Login"
#     html['description']    = "Welcome back. Nice to see you."
#     html['content']        = ""
#
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#
#     form = LoginForm()
#
#     # if form.validate_on_submit():
#     #     user = NetUser.query.filter_by(email=form.email.data).first()
#
#     #     if user is None or not user.check_password(form.password.data):
#     #         flash('Invalid email or password', 'danger')
#     #         return redirect(url_for('login'))
#
#     #     login_user(user, remember=form.remember_me.data)
#     #     next_page = request.args.get('next')
#
#     #     if not next_page or url_parse(next_page).netloc != '':
#     #         next_page = url_for('index')
#     #     return redirect(next_page)
#
#     return render_template('login.html',
#                            html=html,
#                            form=form)
#
#
# # #reset password request
# # @app.route('/reset_password_request', methods=['GET', 'POST'])
# # def reset_password_request():
# #     html = {}
# #     html['title']          = "Reset my password"
# #     html['description']    = "Gimme my password. Thanks."
# #     html['content']        = ""
#
# #     if current_user.is_authenticated:
# #         return redirect(url_for('index'))
#
# #     form = ResetPasswordRequestForm()
#
# #     if form.validate_on_submit():
# #         user = NetUser.query.filter_by(email=form.email.data).first()
# #         if user:
# #             send_email_password_reset(user)
# #         flash('Check your email. We sent your password reset link.')
# #         return redirect(url_for('login'))
#
# #     return render_template('reset_password_request.html',
# #                            html=html,
# #                            form=form)
#
#
# # #reset password
# # @app.route('/reset_password/<token>', methods=['GET', 'POST'])
# # def reset_password(token):
#
# #     html = {}
# #     html['title']          = "Reset my password"
# #     html['description']    = "Gimme my password. Thanks."
# #     html['content']        = ""
#
# #     if current_user.is_authenticated:
# #         return redirect(url_for('index'))
#
# #     user = NetUser.verify_reset_password_token(token)
#
# #     if not user:
# #         return redirect(url_for('index'))
#
# #     form = ResetPasswordForm()
#
# #     if form.validate_on_submit():
# #         user.set_password(form.password1.data)
# #         db.session.commit()
# #         flash('Your password is reset. Login below.')
# #         return redirect(url_for('login'))
#
# #     return render_template('reset_password.html',
# #                            html=html,
#                            # form=form)
#
#
#
#
#
#
#
#
# ##############################
# # AUTHENTICATED
# ##############################
#
# #logout route
# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('index'))
#
#
#
#
# #edit user profile
# @app.route('/profile', methods=['GET', 'POST'])
# @login_required
# def profile():
#
#     html = {}
#     html['title']          = "My Profile"
#     html['description']    = ""
#     html['content']        = ""
#
#     # Get user profile and record
#     user_id = NetUser.user_id
#     user = NetUser.query.filter_by(user_id=user_id).first_or_404()
#
#     form = EditProfileForm()
#
#     if form.validate_on_submit():
#         current_user.first_name = form.first_name.data
#         current_user.last_name = form.last_name.data
#         current_user.email = form.new_email.data
#         current_user.date_updated = datetime.utcnow()
#         db.session.commit()
#         flash('Your profile is updated.', 'success')
#         return redirect(url_for('profile'))
#
#     elif request.method == 'GET':
#         form.first_name.data = current_user.first_name
#         form.last_name.data = current_user.last_name
#         form.new_email.data = current_user.email
#
#     return render_template('profile.html',
#                            html=html,
#                            form=form,
#                            user=user)
