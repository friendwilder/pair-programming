from flask import Flask, request, jsonify, abort
from werkzeug.exceptions import HTTPException
from models import setup_db, User, Appointment

app = Flask(__name__)
setup_db(app)


@app.route('/')
def hello_world():
    return 'Hello, World :P'


'''
    GET /users
        It should NOT be a public endpoint.
        It should contain only the user.short() data representation
    Returns status code 200 and json {"success": True, "users": users}
        where users is the list of users
        or appropriate status code indicating reason for failure
'''


@app.route('/users', methods=['GET'])
def get_users():
    return 'GET not implemented'


'''
    GET /users/<id>
        It should NOT be a public endpoint.
        It should contain only the user.long() data representation
    Returns status code 200 and json {"success": True, "users": users}
        where user an array containing only the requested user
        or appropriate status code indicating reason for failure
'''


@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    return 'GET user not implemented'


'''
    POST /users
        It should NOT be a public endpoint.
        It should contain only the user.long() data representation
    Returns status code 200 and json {"success": True, "users": users}
        where user an array containing only the newly created user
        or appropriate status code indicating reason for failure
'''


@app.route('/users', methods=['POST'])
def add_user():
    body = request.get_json()
    print(body)

    username = body.get('username', None)
    email = body.get('email', None)

    try:
        new_user = User(username=username, email=email)
        new_user.insert()

        return jsonify({
            'success': True,
            'created': new_user.id
        })
    except HTTPException:
        abort(422)
        # return 'POST not implemented'


'''
    PATCH /users/<id>
        It should NOT be a public endpoint.
        It should contain only the user.long() data representation
    Returns status code 200 and json {"success": True, "users": users}
        where user an array containing only the modified user
        or appropriate status code indicating reason for failure
'''


@app.route('/users/<int:id>', methods=['PATCH'])
def update_user(id):
    return 'PATCH not implemented'


'''
    DELETE /users/<id>
        It should NOT be a public endpoint.
        It should contain only the user.short() data representation
    Returns status code 200 and json {"success": True, "users": users}
        where user an array containing only the deleted user
        or appropriate status code indicating reason for failure
'''


@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    return 'DELETE not implemented'