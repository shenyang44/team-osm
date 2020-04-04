from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.employee import Employee
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash


employees_blueprint = Blueprint('employees',
                                __name__,
                                template_folder='templates')


@employees_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('employees/new.html')


@employees_blueprint.route('/', methods=['POST'])
def create():

    email = request.form.get('email')
    email_taken = Employee.get_or_none(Employee.email == email)
    if email_taken:
        flash('Email already taken.', 'danger')
        return redirect(url_for('employees.new'))

    username = request.form.get('username')
    username_taken = Employee.get_or_none(
        Employee.username == username)
    if username_taken:
        flash('Username already taken', 'danger')
        return redirect(url_for('employees.new'))

    password = request.form.get('password')
    hashed_password = generate_password_hash(password)

    signup = Employee(email=email, username=username, password=hashed_password)

    try:
        signup.save()
        flash('Employee successfully signed up', 'success')
        employee = Employee.get_or_none(Employee.username == username)
        login_user(employee)
        return redirect(url_for('events.index'))

    except:
        flash('Error creating Employee', 'danger')
        return redirect(url_for('employees.new'))
