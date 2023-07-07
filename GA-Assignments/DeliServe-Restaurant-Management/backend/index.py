from flask import Flask, jsonify
from flask_socketio import SocketIO, emit
from pymongo import MongoClient
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv
from bson import ObjectId
import json
from flask_cors import CORS

# Load environment variables from .env file
load_dotenv()

# Access the MongoDB connection URL from environment variables
mongo_url = os.getenv("MONGO_URL")

app = Flask(__name__)
app.config['MONGO_URI'] = mongo_url  # Update with your MongoDB connection URI
CORS(app, resources={r"/*": {"origins": "*"}})
mongo = PyMongo(app)
socketio = SocketIO(app)

# Custom JSON encoder for handling ObjectId serialization
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super().default(obj)

# Collection names
users_collection = mongo.db.users
menu_collection = mongo.db.menu
orders_collection = mongo.db.orders

@app.route('/menu', methods=['GET'])
def get_menu():
    menu_cursor = menu_collection.find()
    print(list(menu_cursor))
    menu = [item for item in menu_cursor]
    return jsonify(json.dumps(menu, cls=CustomJSONEncoder))




if __name__ == '__main__':
    socketio.run(app,port=4040)
