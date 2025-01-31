from flask import Blueprint, request, jsonify
from services.monster_service import MonsterService

monster_routes = Blueprint('monster_routes', __name__)

# TODO: add request body validation via Marshmallow schemas


@monster_routes.route('/monsters', methods=['POST'])
def create_monster():
    """
    Create a monster

    Returns:
        _type_: _description_
    """
    try:
        monster_data = request.get_json()
        # TODO: add validation step
        # TODO: this data should conform to an interface type
        monster_data = None
        monster = MonsterService.create_monster(monster_data)
        return jsonify(monster.to_dict()), 201
    
    except Exception as err:
        return jsonify({"error": err.messages}), 500


# Get a single user by ID
@monster_routes.route('/monsters/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())

# Update a user
@monster_routes.route('/monsters/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    db.session.commit()
    return jsonify(user.to_dict())

# Delete a monster
@monster_routes.route('/monsters/<int:id>', methods=['DELETE'])
def delete_user(id):
    # NOTE: all session management should happen in dungeons_logic. Need to 
    # import the package.
    user = Monster.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"}), 204
