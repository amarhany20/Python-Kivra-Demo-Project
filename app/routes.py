from flask import Blueprint, request, jsonify
from .models import db, User, Location, Type, Mail

bp = Blueprint('routes', __name__)

@bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(
        email=data['email'],
        password=data['password'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        age=data.get('age')
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201

@bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({
        'userId': user.userId,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'age': user.age,
        'creation_date': user.creation_date,
        'update_date': user.update_date
    })

# Add more routes similarly
