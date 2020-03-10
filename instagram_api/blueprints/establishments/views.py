from flask import Blueprint, jsonify, request, render_template, redirect, json
from models.blood_invetory import Blood_Inventory
from models.establishment import Establishment
from models.events import Events
# from models.user import User
# from werkzeug.security import generate_password_hash, check_password_hash
from playhouse.shortcuts import model_to_dict
# from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity


establishments_api_blueprint = Blueprint('establishment_api',
                                         __name__,
                                         template_folder='templates')


@establishments_api_blueprint.route('/establishment', methods=['GET'])
def index_establishment():
    establishments = Establishment.select()
    establishment_list = []
    for establishment in establishments:
        establishment = model_to_dict(establishment)
        establishment_list.append(establishment)
    return jsonify(establishment_list)


@establishments_api_blueprint.route('/events', methods=['GET'])
def index_events():
    events = Events.select()
    event_list = []
    for event in events:
        event = model_to_dict(event)
        event_list.append(event)
    return jsonify(event_list)


@establishments_api_blueprint.route('/blood_inventory', methods=['GET'])
def index_blood_inventory():
    blood_inventory = Blood_Inventory.select()
    blood_inventory_list = []
    for blood_inventory in blood_inventory:
        blood_inventory = model_to_dict(blood_inventory)
        blood_inventory_list.append(blood_inventory)
    return jsonify(blood_inventory_list)
