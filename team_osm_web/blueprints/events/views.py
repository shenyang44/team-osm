from flask import Blueprint, render_template, redirect, request, url_for, flash
from models.events import Event
from models.establishment import Establishment
from flask_login import login_required

events_blueprint = Blueprint('events',
                             __name__,
                             template_folder='templates')


@events_blueprint.route('/', methods=['GET'])
@login_required
def index():
    # event = Event.select()
    # establishment = Establishment.select()
    return render_template('events/index.html')

# @events_blueprint.route('/', methods=['GET'])
# def show():
#     # events = Event.select()
#     # establishments = Establishment.select()
#     return render_template('events/index.html')


@events_blueprint.route('/new', methods=['GET'])
@login_required
def new():
    establishments = Establishment.select()
    return render_template('events/new_events.html', establishments=establishments)


@events_blueprint.route('/create', methods=['POST'])
@login_required
def create():
    location = request.form.get('location')
    date = request.form.get('date')
    time = request.form.get('time')
    event_name = request.form.get('event_name')
    description = request.form.get('description')
    establishment_id = request.form.get('establishment_id')

    events = Event(location=location, date=date, time=time, event_name=event_name,
                   description=description, establishment_id=establishment_id)

    try:
        events.save()
        flash('Event registered successfully', 'success')
        return redirect(url_for('events.index'))

    except:
        flash('Error creating event', 'danger')
        return redirect(url_for('events.new'))


@events_blueprint.route('/delete/<id>')
def delete(id):
    event = Event.get_or_none(Event.id == id)
    if event.delete_instance():
        return redirect(url_for('events.index'))
    else:
        flash('Sorry but the deletion could not be executed', 'danger')
        return redirect(url_for(request.referrer))
