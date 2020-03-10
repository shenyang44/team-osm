from flask import Blueprint, render_template, request, url_for, redirect
from models.establishment import Establishment
from models.events import Events
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

    establishment = Establishment(name=name, address=address)

    try:
        establishment.save()
        # flash('Establishment registered successfully', 'success')
        return redirect(url_for('home'))

    except:
        # flash('Error creating Establishment', 'danger')
        return redirect(url_for('establishments.new_establishment'))


@establishments_blueprint.route('/events', methods=['GET'])
def new_events():
    establishments = Establishment.select()
    return render_template('establishments/new_events.html', establishments=establishments)


@establishments_blueprint.route('/events/', methods=['POST'])
def create_events():
    location = request.form.get('location')
    date = request.form.get('date')
    time = request.form.get('time')
    event_name = request.form.get('event_name')
    description = request.form.get('description')
    establishment_id = request.form.get('establishment_id')

    events = Events(location=location, date=date, time=time, event_name=event_name,
                    description=description, establishment_id=establishment_id)

    try:
        events.save()
        # flash('Establishment registered successfully', 'success')
        return redirect(url_for('home'))

    except:
        # flash('Error creating Establishment', 'danger')
        return redirect(url_for('establishments.new_events'))


@establishments_blueprint.route('/blood_inventory', methods=['GET'])
def new_blood_inventory():
    establishments = Establishment.select()
    return render_template('establishments/new_blood_inventory.html', establishments=establishments)


@establishments_blueprint.route('/blood_inventory/', methods=['POST'])
def create_blood_inventory():
    blood_type = request.form.get('blood_type')
    quantity = request.form.get('quantity')
    establishment_id = request.form.get('establishment_id')

    blood_inventory = Blood_Inventory(blood_type=blood_type, quantity=quantity,
                                      establishment_id=establishment_id)

    try:
        blood_inventory.save()
        # flash('Establishment registered successfully', 'success')
        return redirect(url_for('home'))

    except:
        # flash('Error creating Establishment', 'danger')
        return redirect(url_for('establishments.new_blood_inventory'))
