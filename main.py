from flask import Flask, jsonify, request

app = Flask(__name__)


user_list = [
    {
        "username": "abc",
        "password": "abc"
    },
    {
        "username": "123",
        "password": "123"
    },
]


@app.route("/")
def hello_world():
    return "Hello, World!!!!!!!"


@app.get("/users")
def get_all_users():
    return jsonify(user_list)


@app.post('/new-user')
def new_user():
    new_user = request.get_json()
    user_list.append(new_user)
    return jsonify({'message': 'user created', 'method': request.method})


@app.delete('/<username>')
def del_user(username):
    for user in user_list:
        if username == user.get('username'):
            user_list.remove(user)
    return jsonify({'message': 'user deteled'})
