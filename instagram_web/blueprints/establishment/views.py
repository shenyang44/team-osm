from flask import Blueprint, render_template
from models.establishment import Establishment

establishments_blueprint = Blueprint('establishments',
                                     __name__,
                                     template_folder='templates')


@establishments_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('establishment/new.html')


@establishments_blueprint.route('/', methods=['POST'])
def create():
    name = request.form.get('name')
    address = request.form.get('address')

    establishment = Establishment(name=name, address=address)

    try:
        establishment.save()
        # flash('Establishment registered successfully', 'success')
        return redirect(url_for('establishment.new'))

    except:
        # flash('Error creating Establishment', 'danger')
        return redirect(url_for('establishment.new'))
