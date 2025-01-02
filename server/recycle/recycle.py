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

@app.route('/users', methods=['GET', 'POST'])
def all_users():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        USERS.append({
            'id': uuid.uuid4().hex,
            'username': post_data.get('username'),
            'password': post_data.get('password'),
            'role': post_data.get('role'),
            'created-at': post_data.get('created-at'),
        })
        response_object['message'] = 'Users added!'
    else:
        response_object['users'] = USERS
    return jsonify(response_object)

@app.route('/rules/<rule_id>', methods=['PUT', 'DELETE'])
def single_rule(rule_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        put_data = request.get_json()
        remove_rule(rule_id)
        RULES.append({
            'id': uuid.uuid4().hex,
            'remark': put_data.get('remark'),
            'source': put_data.get('source'),
            'destination': put_data.get('destination'),
            'port': put_data.get('port'),
            'action': put_data.get('action'),
        })
        response_object['message'] = 'Rule updated!'
    if request.method == 'DELETE':
        remove_rule(rule_id)
        response_object['message'] = 'Rule removed!'
    return jsonify(response_object)

@app.route('/users/<user_id>', methods=['PUT', 'DELETE'])
def single_user(user_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        put_data = request.get_json()
        remove_user(user_id)
        USERS.append({
            'id': uuid.uuid4().hex,
            'username': put_data.get('username'),
            'password': put_data.get('password'),
            'role': put_data.get('role'),
            'created-at': put_data.get('created-at'),
        })
        response_object['message'] = 'User updated!'
    if request.method == 'DELETE':
        remove_user(user_id)
        response_object['message'] = 'User removed!'
    return jsonify(response_object)
    
def remove_rule(rule_id):
    for rule in RULES:
        if rule['id'] == rule_id:
            RULES.remove(rule)
            return True
    return False

def remove_user(user_id):
    for user in USERS:
        if user['id'] == user_id:
            USERS.remove(user)
            return True
    return False


RULES = [
    {
        'id': uuid.uuid4().hex,
        'remark': '0001 - RYK',
        'source': '10.20.228.0/22',
        'destination': '10.43.16.114, 10.43.16.117',
        'port': 'tcp/1525',
        'action': True
    },
    {
        'id': uuid.uuid4().hex,
        'remark': '0002 - IMD',
        'source': '10.21.33.161, 10.21.33.150, 10.21.33.224',
        'destination': '10.27.2.126, 10.27.2.127, 10.27.2.13',
        'port': 'tcp/443, tcp/995, tcp/587, tcp/25',
        'action': True
    },
    {
        'id': uuid.uuid4().hex,
        'remark': '0003 - SMJ',
        'source': '10.43.4.221',
        'destination': '10.43.58.77',
        'port': 'udp/1434',
        'action': True
    },
]

USERS = [
    {
        'id': uuid.uuid4().hex,
        'username': 'admin',
        'password': 'admin',
        'role': 'admin',
        'created-at': '02-10-2001 03:15:32 PM'
    },
    {
        'id': uuid.uuid4().hex,
        'username': 'operator_hsk',
        'password': 'hsk',
        'role': 'operator',
        'created-at': '12-02-2023 02:55:12 PM'
    },
    {
        'id': uuid.uuid4().hex,
        'username': 'probation_ryk',
        'password': 'ryk',
        'role': 'probation',
        'created-at': '02-09-2024 09:05:10 PM'
    },
    {
        'id': uuid.uuid4().hex,
        'username': 'guest',
        'password': 'guest',
        'role': 'guest',
        'created-at': '03-10-2001 10:15:30 PM'
    }   
]