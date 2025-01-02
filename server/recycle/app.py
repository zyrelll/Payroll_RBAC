from flask import Flask, jsonify, request, Response
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user
import uuid
from flask_bcrypt import Bcrypt
from sqlalchemy.ext.declarative import DeclarativeMeta
import json

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SECRET_KEY"] = "secretz"
# enable CORS
CORS(app)

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.init_app(app)

# database
class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique = True, nullable = False)
    password = db.Column(db.String(50), nullable = False)
    role = db.Column(db.String(50), nullable = False)
    # jabatan = db.Column(db.String(50), nullable = True)
    # employed_at = db.Column(db.DateTime, nullable = True)
    
class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__,  DeclarativeMeta):
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            return fields

        return json.JSONEncoder.default(self, obj)
    
def conv_func(list_data):
    dic = {  
        "id":list_data[0],
        "username":list_data[1],
        "password":list_data[2],
        "role":list_data[3]
    }
    return dic

db.init_app(app)

with app.app_context():
    db.create_all()

# user loader callback, returns the user object given an id
@login_manager.user_loader
def loader_user(user_id):
    return Users.query.get(user_id)

# sanity check route
@app.route('/register', methods=["POST"])
def register():
    response_object = {'status': 'success'}
    post_data = request.get_json()
# If the user made a POST request, create a new user
    user = Users(username=post_data.get("username"),
                password=post_data.get("password"),
                role=post_data.get("role"))
    # Add the user to the database
    db.session.add(user)
    # Commit the changes made
    db.session.commit()
    # Once user account created, redirect them
    # to login route (created later on)
    return jsonify(response_object)


@app.route("/logout")
def logout():
    response_object = {'status': 'success'}
    logout_user()
    response_object['message'] = 'Logout success!'
    return jsonify(response_object)

@app.route("/auth", methods=["GET", "POST"])
def all_auth():    
    response_object = {'status': 'success'}
    post_data = request.get_json()
    user = Users.query.filter_by(
        username = post_data.get("username")).first()
    if request.content_type != 'application/json':
            return jsonify({"bjir pusing!!!!!!!!!!!!!!!!"}), 415
    elif request.method == 'GET':

        # data = json.loads(user)
        # new_data = []
        # for i in data:
        #     new_data.append(conv_func(i))
        # temp = user 
        converted_data = json.dumps(user, cls=AlchemyEncoder)
        # # response_object['user'] = user
        return Response(converted_data, mimetype='application/json')
        # response_object['user'] = user
    elif request.method == 'POST':
        if user.password ==  post_data.get("password") :
            login_user(user)
            converted_data = json.dumps(user, cls=AlchemyEncoder)
            return Response(converted_data, mimetype='application/json')
            # response_object['user'] = user
    
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()