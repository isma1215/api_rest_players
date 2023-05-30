from functools import wraps
import jwt
from flask import request , jsonify
from flask import current_app as app
from models.Model_User import Model_User
from models.Player import ModelPlayer

def token_marter(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
        if not token:
            return {"message":"token is messing!"} ,401
        
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"],algorithms=["HS256"])
            user = Model_User.get_for_id(data["user_id"])
            
            if user is None:
                return {"message":"token invalidate"}
            
            if not user["master"]:
                return {"message":"no tienes acceso"}
            
        except Exception as ex:
            return jsonify({'message':str(ex)}),500
        
       
        return f(user,*args,**kwargs)
    
    return decorated

def access_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
        if not token:
            return {"message":"token is messing!"} ,401
        
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"],algorithms=["HS256"])
            user = Model_User.get_for_id(data["user_id"])
            
            if user is None:
                return {"message":"token invalidate"}

            if user["master"]:
                return user
            
            if request.method == "POST":
                if user["soccer_team"] != request.json["soccer_team"]:
                    return {'message':'You can only modify or access data from your team'}
                
            if request.method == "GET":
                if kwargs:
                    player = ModelPlayer.get_player_by_id(kwargs["id"])
                    if user["soccer_team"] != player["soccer_team"]:
                        return {'message':'You can only modify or access data from your team'}
             
            if request.method == ("PUT" or "DELETE"):
                player = ModelPlayer.get_player_by_id(kwargs["id"])
                
                if user["soccer_team"] != player["soccer_team"]:
                    return {'message':'You can only modify or access data from your team'}
            
        except Exception as ex:
            return jsonify({'message':str(ex)}),500
        
       
        return f(user,*args,**kwargs)
    
    return decorated



