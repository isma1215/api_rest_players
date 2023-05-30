from flask import Blueprint,jsonify
from models.Team import Model_Team
teams = Blueprint('teams_blueprint', __name__)

@teams.route('/', methods=['GET'])
def get_teams():
    try:
        teams = Model_Team.get_teams()
        return teams
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@teams.route('/<id>')
def get_one_team(id):
    try:
        teams = Model_Team.get_one_team(id)
        return teams
    except Exception as ex:
        return jsonify({'message': str(ex)}) , 500
