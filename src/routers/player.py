from flask import Blueprint, jsonify,request
from models.Player import ModelPlayer 
from models.entities.Player import Player
from middleware.auth_middleware import access_token , token_marter
import uuid

main = Blueprint('player_blueprint',__name__)

@main.route('/all')
@token_marter
def get_player(user):
    try:
        players = ModelPlayer.get_players()
        return players
    except Exception as ex:

        return jsonify({'message':str(ex)}), 500

@main.route('/')
@access_token
def get_team_player(user):
    try:
        players = ModelPlayer.get_players_my_team(user)
        return players
    except Exception as ex:
        return jsonify({'message':str(ex)}), 500 
    
@main.route('/<id>')
@access_token
def get_team_playe(user,id):
    try:
        player = ModelPlayer.get_one_player(id)
        return  player
    
    except Exception as ex:
        return jsonify({'message':str(ex)}), 500 

@main.route('/add', methods = ['POST'])
@access_token
def add_player(user):
    
    try:
        P = request.json
        url_default = '/upload/img/default.jpg'
        player = Player(str(uuid.uuid4()) ,P['name'],P['last_name'],P['jersey_number'],P['birthday'],url_default,P['soccer_team'])
        
        affected_row = ModelPlayer.add_player(player)
        if affected_row == 1 :
            return jsonify({'message':'player added'}),200
        else:
            return jsonify({'message':'error on insert'}) ,200
    except Exception as ex:
        return jsonify({'message': str(ex)}) ,500


@main.route('/update/<id>', methods=['PUT'])
@access_token
def update_player(user,id):
    try:
        P = request.json
        player = Player(id,P['name'],P['last_name'],P['jersey_number'])
        affected_row = ModelPlayer.update_player(player)

        if affected_row == 1:
            return jsonify({"message":"playerd update"})
        else:
            jsonify({"message": 'error on update'})

    except Exception as ex:
        return jsonify({'message': str(ex)}) ,500


@main.route('/delete/<id>', methods =['DELETE'])
@access_token
def delete_player(user,id):
    try:
        player = Player(id)
        affected_row = ModelPlayer.delete_player(player)
        if affected_row == 1:
            return jsonify({'message':"player delete"})
        else:
            return jsonify({"message":"error player not delete"}) ,404
        
    except Exception as ex:
        return jsonify({'message':str(ex)}) ,500


"""@main.route('/<name>')
def get_player_for_name(name):
    try:
        player = ModelPlayer.get_player_for_name(name)
        if player != None:
            return jsonify(player)
        else:
            return jsonify({'message':'not found'}) , 404
    except Exception as ex:
        return jsonify({'message':str(ex)}), 500"""