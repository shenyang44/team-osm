from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash
from models.employee import Employee
from flask_login import LoginManager, current_user, login_user, login_required, logout_user


sessions_blueprint = Blueprint('sessions',
                               __name__,
                               template_folder='templates')


@sessions_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('sessions/new.html')


@sessions_blueprint.route('/', methods=['POST'])
def loggin():

    if current_user.is_authenticated:
        return redirect(url_for('home'))

    password_to_check = request.form.get('password')
    username = request.form.get('username')

    user = Employee.get_or_none(Employee.username == username)

    if not user:
        flash("We don't seem to have you in our system. Please doublecheck your name.")
        return redirect(url_for('sessions.new'))

    hashed_password = user.password

    if not check_password_hash(hashed_password, password_to_check):
        flash("That password is incorrect")
        return redirect(url_for('sessions.new'))

    login_user(user)
    flash('Login Successful', 'success')
    return redirect(url_for('home'))


@sessions_blueprint.route("/settings")
@login_required
def settings():
    pass


@sessions_blueprint.route("/logout")
@login_required
def logout():
    logout_user()

    try:
        # session["user_id"] = user.id
        flash('Logout Successful', 'success')
        return redirect(url_for('home'))

    except:
        flash('Logout Failed, you cant leave(remember to call the function for the href)', 'danger')
        return redirect(url_for('home'))
