from flask import Blueprint, jsonify, request, render_template, redirect, json
from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

users_api_blueprint = Blueprint('users_api',
                                __name__,
                                template_folder='templates')


@users_api_blueprint.route('/', methods=['GET'])
def index():
    users = User.select()
    user_list = []
    for user in users:
        data = user.__dict__
        user_list.append(data['__data__'])
    return jsonify(user_list)


@users_api_blueprint.route('/create', methods=['POST'])
def create():
    resp = request.get_json()
    name = resp.get('name')
    password = resp.get('password')
    email = resp.get('email')
    number = resp.get('number')
    hashed_pa = generate_password_hash(password)
    user = User(name=name, password=hashed_pa, email=email, number=number)
    if user.save():
        return jsonify({
            "message": 'fudge you, it worked'
        })
    else:
        return
