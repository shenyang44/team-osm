from flask import Blueprint, jsonify, request, render_template, redirect, json
from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from playhouse.shortcuts import model_to_dict

from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

users_api_blueprint = Blueprint('users_api',
                                __name__,
                                template_folder='templates')


@users_api_blueprint.route('/', methods=['GET'])
def index():
    users = User.select()
    user_list = []
    for user in users:
        user = model_to_dict(user)
        user_list.append(user)
    return jsonify(user_list)


@users_api_blueprint.route('/show', methods=['GET'])
@jwt_required
def show():
    user_id = get_jwt_identity()
    # current_user = User.get_or_none(User.id == user_id)
    # return jsonify(name=current_user.name, email=current_user.email, address=current_user.address, number=current_user.number, blood=current_user.blood_group)
    return jsonify(message='wanker')


@users_api_blueprint.route('/sign-up', methods=['POST'])
def create():
    resp = request.get_json()
    name = resp.get('name')
    password = resp.get('password')
    email = resp.get('email')
    number = resp.get('number')
    address = resp.get('address')
    hashed_pa = generate_password_hash(password)
    blood_type = resp.get('bloodType')
    user = User(name=name, password=hashed_pa,
                email=email, number=number, address=address, blood_group=blood_type)

    if user.save():
        user = User.get_or_none(User.email == email)
        access_token = create_access_token(identity=user.id)
        return jsonify({
            "message": 'fudge you, it worked',
            "access_token": access_token
        })
    else:
        return jsonify({
            'message': user.errors
        })


# @users_api_blueprint.route('/login', methods=['POST'])
# def login():
#     if not request.is_json:
#         return jsonify({"msg": "Missing JSON in request"}), 400
#     email = request.json.get('email', None)
#     password = request.json.get('password', None)
#     if not email:
#         return jsonify({"msg": "Missing username parameter"}), 400
#     if not password:
#         return jsonify({"msg": "Missing password parameter"}), 400

#     user = User.get_or_none(User.email == email)
#     # if username != 'test' or password != 'test':
#     #     return jsonify({"msg": "Bad username or password"}), 401

#     access_token = create_access_token(identity=user.id)
#     return jsonify(access_token=access_token), 200


# Protect a view with jwt_required, which requires a valid access token
# in the request to access.
# @app.route('/protected', methods=['GET'])
# @jwt_required
# def protected():
#     # Access the identity of the current user with get_jwt_identity
#     current_user = get_jwt_identity()
#     return jsonify(logged_in_as=current_user), 200
