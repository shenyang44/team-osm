from flask import Blueprint, render_template, request, url_for, redirect, flash
from models.establishment import Establishment
from models.events import Event
from models.blood_invetory import Blood_Inventory


establishments_blueprint = Blueprint('establishments',
                                     __name__,
                                     template_folder='templates')


@establishments_blueprint.route('/new', methods=['GET'])
def new_establishment():
    return render_template('establishments/new_establishment.html')


@establishments_blueprint.route('/', methods=['POST'])
def create_establishment():
    name = request.form.get('name')
    address = request.form.get('address')
    hospital_type = request.form.get('hospital_type')

    establishment = Establishment(
        name=name, address=address, hospital_type=hospital_type)

    try:
        establishment.save()
        flash('Establishment registered successfully', 'success')
        return redirect(url_for('home'))

    except:
        flash('Error creating Establishment', 'danger')
        return redirect(url_for('establishments.new_establishment'))


@establishments_blueprint.route('/blood_inventory', methods=['GET'])
def new_blood_inventory():
    establishments = Establishment.select()
    return render_template('establishments/new_blood_inventory.html', establishments=establishments)


@establishments_blueprint.route('/blood_inventory/create', methods=['POST'])
def create_blood_inventory():
    blood_type = request.form.get('blood_type')
    quantity = request.form.get('quantity')
    establishment_id = request.form.get('establishment_id')

    blood_inventory = Blood_Inventory(blood_type=blood_type, quantity=quantity,
                                      establishment_id=establishment_id)

    try:
        blood_inventory.save()
        flash('Establishment registered successfully', 'success')
        return redirect(url_for('home'))

    except:
        flash('Error creating Establishment', 'danger')
        return redirect(url_for('establishments.new_blood_inventory'))
