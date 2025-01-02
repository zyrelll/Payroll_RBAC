from flask import (
    Flask, jsonify, request, make_response
)

from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt,
    get_jwt_identity, set_access_cookies, unset_jwt_cookies
)

from datetime import timedelta
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import DeclarativeMeta
from passlib.hash import sha256_crypt
import json

from flask import Flask, jsonify, request
from flask_cors import CORS

#INITIALIZE THE APP#
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite" 
#Using SQLALCHEMY database for this project

app.config["JWT_SECRET_KEY"] = "c2e3ac86102257b59f176d2506e6739afa030f0a"
#This secret key is mandatory to generate and verify jwt token. It should never be exposed to public

app.config['JWT_TOKEN_LOCATION'] = ['cookies']
#default = headers. JWT token can be fetched from headers, cookies (best practice), query_string, json

app.config['JWT_COOKIE_CSRF_PROTECT'] = True
#True in production

#app.config['JWT_COOKIE_SECURE'] = False
#The cookies will only be sent over a HTTPS connection, default = false

# app.config['JWT_ACCESS_COOKIE_PATH'] = '/
#The path for access cookies. default = '/'

# app.config['JWT_COOKIE_SAMESITE'] = 'None'
#Controls whether or not a cookie is sent with cross-site requests, providing some protection against cross-site request forgery attacks (CSRF).
#Strict = browser sends the cookie only for same-site requests. 
#Lax = Cookies is sent when user navigate to origin site from external site.
#None = No restriction but the 'Secure' attribute must be set 
#To use SameSite=None, you must set this option to the string "None" as well as setting JWT_COOKIE_SECURE to True.
#default = 'Lax'

jwt = JWTManager(app)

CORS(app, support_credentials=True, resources={r"/*": {"origins": "http://localhost:5173"}})
#Cross-Origin Resource Sharing, only allow load resource from written origins above
#support_credentials=True is used to allow cookies or authenticated requests to be made cross origins

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
    
#DATABASE#
db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique = True, nullable = False)
    password = db.Column(db.String(50), nullable = False)
    role = db.Column(db.String(50), nullable = False)
    
db.init_app(app)
with app.app_context():
    db.create_all()

#ROUTING
@app.route("/register", methods=["POST"])
def register():
    post_username = request.json.get("username", None)
    post_password = request.json.get("password", None)
    post_role = request.json.get("role", None)
    
    hashed_password = sha256_crypt.hash(post_password)
    
    user = Users(username=post_username,
                password=hashed_password,
                role=post_role)
    
    db.session.add(user)
    db.session.commit()
    
    return jsonify({"msg": "Registration Success"}), 200
#add try except 

@app.route("/login", methods=["POST"])
def login():
    post_username = request.json.get("username", None)
    post_password = request.json.get("password", None)
    user = Users.query.filter_by(
        username = post_username
    ).first()

    if not sha256_crypt.verify(post_password, user.password):
        return jsonify({"msg": "Invalid username or password"}), 401
    
    additional_claims = {"role": user.role}
    
    # converted_data = json.dumps(user, cls=AlchemyEncoder)

    access_token = create_access_token(identity=post_username, additional_claims=additional_claims, expires_delta=timedelta(hours=1))
    # refresh_token = create_refresh_token(identity=post_username, )
    # Response.set_cookie('access_token_cookie', access_token, max_age=None, expires=None, path='/', domain=None, secure=False, httponly=True, samesite=None, partitioned=False)
    resp = jsonify({'msg': "Login successful"})
    set_access_cookies(resp, access_token)
    # set_refresh_cookies(resp, refresh_token)
    # resp.set_cookie('access_token_cookie', access_token, httponly=True)
    return resp, 200
    # return Response(converted_data, mimetype='application/json')
#add try except 

@app.route('/token/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    # Create the new access token
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)

    # Set the JWT access cookie in the response
    resp = jsonify({'refresh': True})
    set_access_cookies(resp, access_token)
    return resp, 200

@app.route('/token/remove', methods=['POST']) #ini untuk logout, DONE
def logout():
    resp = jsonify({'logout': True})
    unset_jwt_cookies(resp)
    return resp, 200

@app.route('/api/example', methods=['GET'])
@jwt_required()
def protected():
    username = get_jwt_identity()
    return jsonify({'hello': 'from {}'.format(username)}), 200

@app.route('/setCookiesRoleFromJWT', methods=['GET'])
@jwt_required()
#@verify_jwt_in_request
def setRole():
    csrf_cookie = request.cookies.get('csrf_access_token')
    if not csrf_cookie:
        return jsonify({'message': 'invalid csrf cookies'})
    claims = get_jwt()
    resp = make_response('setting role cookies')
    resp.set_cookie('role', claims['role'])
    return resp , 200

# @app.route("/protected", methods=["GET"])
# @jwt_required()
# def protected():
#     current_user = get_jwt_identity()
#     return jsonify(logged_in_as=current_user), 200

# @app.route("/protectedAddRole", methods=["GET"])
# @jwt_required()
# def protected():
#     claims = get_jwt()
#     return jsonify(claims["role"])


# store jwt in local storage and access via auth headers

# async function login() {
#   const response = await fetch('/login_without_cookies', {method: 'post'});
#   const result = await response.json();
#   localStorage.setItem('jwt', result.access_token);
# }

# function logout() {
#   localStorage.removeItem('jwt');
# }

# async function makeRequestWithJWT() {
#   const options = {
#     method: 'post',
#     headers: {
#       Authorization: `Bearer ${localStorage.getItem('jwt')}`,
#     }
#   };
#   const response = await fetch('/protected', options);
#   const result = await response.json();
#   return result;
# }