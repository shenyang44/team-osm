from flask import Blueprint, jsonify, request, render_template, redirect
from models.user import User


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
    resp = request.get('http://localhost: 5000/api/v1/users/create')
    return render_template('new.html', response=resp.json)
