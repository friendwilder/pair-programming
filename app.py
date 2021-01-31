from flask import Flask, request, jsonify, abort
from flask_migrate import current
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
    try:
        users_list = User.query.all()
        users_list = [user.format() for user in users_list]

        return jsonify({
            'success': True,
            'users': users_list
        })
    except Exception:
        abort(422)


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
    try:
        current_user = User.query.get(id)
        current_user = current_user.format()
        return jsonify({
            'success': True,
            'user': current_user
        })
    except Exception:
        abort(422)


'''
    POST /users
        It should NOT be a public endpoint.
        It should contain only the user.long() data representation
    Returns status code 200 and json {"success": True, "users": users}
        where user an array containing only the newly created user
        or appropriate status code indicating reason for failure
'''


@app.route('/appointments', methods=['POST'])
def add_user():
    body = request.get_json()

    user_id = body.get('id', None)
    appointment_time = body.get('appointment_time', None)

    try:
        new_appointment = Appointment(appointment_time=appointment_time)
        new_appointment.hosting_user.append(User.query.get(user_id))
        new_appointment.insert()

        return jsonify({
            'success': True,
            'created': new_appointment.id
        })
    except HTTPException:
        abort(422)


'''
    PATCH /users/<id>
        It should NOT be a public endpoint.
        It should contain only the user.long() data representation
    Returns status code 200 and json {"success": True, "users": users}
        where user an array containing only the modified user
        or appropriate status code indicating reason for failure
'''


@app.route('/appointments/<int:id>', methods=['PATCH'])
def update_appointment(id):
    body = request.get_json()
    updated_time = body.get('updated_time', None)

    try:
        appointment = Appointment.query.get(id)
        if appointment is None:
            abort(404)
        appointment.appointment_time = updated_time
        appointment.update()
        return jsonify({
            'success': True,
            'id': appointment.id,
            'updated_time': appointment.appointment_time
        })
    except Exception:
        abort(422)


'''
    DELETE /users/<id>
        It should NOT be a public endpoint.
        It should contain only the user.short() data representation
    Returns status code 200 and json {"success": True, "users": users}
        where user an array containing only the deleted user
        or appropriate status code indicating reason for failure
'''


@app.route('/appointments/<int:id>', methods=['DELETE'])
def delete_appointment(id):
    try:
        appointment = Appointment.query.get(id)
        appointment.delete()
        return jsonify({
            'success': True,
            'deleted': id
        })
    except Exception:
        abort(422)  