from flask import Blueprint,jsonify,request
from flask import current_app as app
from models.Model_User import Model_User
from models.entities.User import User as User_entities
from middleware.auth_middleware import token_marter
import jwt
import uuid

User = Blueprint('User_blueprint',__name__)


@User.route('/all')
@token_marter
def users(user):
    try:
        users = Model_User.get_all_users()
        return users
    
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@User.route('/<name>')
def user(name):
    try:
        user = Model_User.get_for_name(name)
        return user
    
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@User.route('/add',methods=['POST'])
@token_marter
def add_user(user):
    try:
        data = request.json
        new_user = User_entities(str(uuid.uuid4()),data["name"],data["password"],None,data["soccer_team"] )
        affected_row = Model_User.add_user(new_user)
        
        if affected_row == 1 :
            return jsonify({"message":"User add","data":new_user.to_Json()}) , 200
        else:
            return jsonify({'message':'error on insert'}) ,200
    
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
    
@User.route('/delete/<id>', methods=["DELETE"])
@token_marter
def delete_user(id):
    try:
        user = User_entities(id)
        affected_row = Model_User.delete_user(user)
        if affected_row == 1:
            return jsonify({"message":"user delete","id":id}) , 200
        else:
            return jsonify({"message":"user not delete","id":id}) , 200
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
    
@User.route('/update/<id>', methods=["PUT"])
def update_user(id):
    try:
        data = request.json
        user = User_entities(id,data["name"],data["password"],None,data["soccer_team"])
        affected_row = Model_User.update(user)
        if affected_row == 1:
            return jsonify({"message":"user is update","id":id}) , 200
        else:
            return jsonify({"message":"user not update","id":id}) , 200
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
    
    
@User.route('/login', methods=["POST"])
def login():
    try:
        data = request.json
        
        if not data:
            return {"message":"Please provide user details"}
        
        user = Model_User.login(data["name"],data["password"])
        if not user:
            return{"message":"Contraseña o usuario es incorrecto"}
        
        if user:
            user["token"] = jwt.encode(
                {"user_id":user["id"],"soccer_team":user["soccer_team"]},
                app.config["SECRET_KEY"],
                algorithm="HS256")
            return user
    
    except Exception as ex:
        return jsonify({'message':str(ex)}),500