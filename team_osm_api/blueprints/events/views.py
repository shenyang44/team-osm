from flask import Blueprint, jsonify, request, render_template, redirect, json
from models.events import Events
from werkzeug.security import generate_password_hash, check_password_hash
from playhouse.shortcuts import model_to_dict
from models.events import Event
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

events_api_blueprint = Blueprint('events_api',
                                 __name__,
                                 template_folder='templates')


@events_api_blueprint.route('/', methods=['GET'])
def index():
    events = Event.select()
    event_list = []
    for event in events:
        event = model_to_dict(event)
        event_list.append(event)
    return jsonify(event_list)
