from flask import Flask, jsonify
from config import config
from routers import player,uploadingimg,routes_teams, routes_Users
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

def page_not_found(error):
    return jsonify({'message': 'the Url does not exist' , 'status' : '404'})


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_blueprint(player.main, url_prefix='/api/players')
    app.register_blueprint(routes_teams.teams,url_prefix='/api/teams')
    app.register_blueprint(uploadingimg.image, url_prefix='/upload')
    app.register_blueprint(routes_Users.User, url_prefix='/api/user')
    app.register_error_handler(404,page_not_found)
    app.run()
