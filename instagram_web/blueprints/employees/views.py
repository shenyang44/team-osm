from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.employee import Employee
from models.events import Events
from models.establishment import Establishment
from flask_login import LoginManager, current_user, login_user, login_required, logout_user

employees_blueprint = Blueprint('employees',
                                __name__,
                                template_folder='templates')


@employees_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('employees/new.html')


@employees_blueprint.route('/', methods=['POST'])
def create():

    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')

    signup = Employee(email=email, username=username, password=password)
    try:
        signup.save()
        employee = Employee.get_or_none(Employee.username == username)
        login_user(employee)
        flash('Employee successfully signed up', 'success')
        return redirect(url_for('employees.show_feed'))

    except:
        flash('Error creating Employee', 'danger')
        return redirect(url_for('employees.new'))


@employees_blueprint.route('/')
@login_required
def show_mainpage():
    event = Events.select()
    establishment = Establishment.select()
    return render_template('employees/main_page.html', event=event, establishment=establishment)
