from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

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

# parser = reqparse.RequestParser()
# parser.add_argument()

class HelloWorld(Resource):
    def get(self):
        return 'hello world', 200


class UserList(Resource):
    def get(self):
        return user_list


api.add_resource(HelloWorld, '/')
# api.add_resource(User, '/user/<string:username>')
api.add_resource(UserList, '/users')