from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import uuid
import os
from dotenv import load_dotenv
from bson import ObjectId
import json


# Load environment variables from .env file
load_dotenv()

# Access the MongoDB connection URL from environment variables
mongo_url = os.getenv("MONGO_URL")

app = Flask(__name__)
app.config['MONGO_URI'] = mongo_url  # Update with your MongoDB connection URI
mongo = PyMongo(app)

# Custom JSON encoder for handling ObjectId serialization
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super().default(obj)

app.json_encoder = CustomJSONEncoder

def generate_order_id():
    unique_id = uuid.uuid4().hex  # Generate a unique ID using UUID
    return f"ORDER-{unique_id}"

# Route to get the entire menu
@app.route('/menu', methods=['GET'])
def get_menu():
    menu = list(mongo.db.menu.find())
    return jsonify(menu)

# Route to get a specific dish from the menu
@app.route('/menu/<dish_id>', methods=['GET'])
def get_dish(dish_id):
    dish = mongo.db.menu.find_one({'_id': ObjectId(dish_id)} )
    if dish:
        return jsonify(dish)
    else:
        return jsonify({'message': 'Dish not found'})

# Route to add a new dish to the menu
@app.route('/menu', methods=['POST'])
def add_dish():
    dish = request.json
    dish['availability']=True
    mongo.db.menu.insert_one(dish)
    return jsonify({'message': 'Dish added successfully'})

# Route to remove a dish from the menu
@app.route('/menu/<dish_id>', methods=['DELETE'])
def remove_dish(dish_id):
    result = mongo.db.menu.find_one_and_delete({'_id': ObjectId(dish_id)})
    if result:
        return jsonify({'message': 'Dish removed successfully'})
    else:
        return jsonify({'message': 'Dish not found'})


# Route to update the availability of a dish
@app.route('/menu/<dish_id>', methods=['PUT'])
def update_availability(dish_id):
    # dish_id = request.json['dish_id']
    # availability = request.json['availability']
    dish = mongo.db.menu.find_one({'_id': ObjectId(dish_id)})
    if dish['availability'] == True:
        mongo.db.menu.update_one(
                {'_id': ObjectId(dish_id)},
                {'$set': {'availability': False}}
            )
    else:
        mongo.db.menu.update_one(
                {'_id': ObjectId(dish_id)},
                {'$set': {'availability': True}}
            )
    return jsonify({'message': 'Availability updated successfully'})

# Route to take a new order from a customer
@app.route('/orders', methods=['POST'])
def new_order():
    customer_name = request.json['customer_name']
    dish_ids = request.json['dish_ids']

    # order_id = generate_order_id()  # Implement a function to generate a unique order ID
    order_status = 'received'

    # Verify dish availability
    for dish_id in dish_ids:
        dish = mongo.db.menu.find_one({'_id':  ObjectId(dish_id)})
        if not dish or not dish['availability']:
            return jsonify({'message': f'Dish {dish_id} is not available'})

    # Process the order and store it in the database
    order = {
        
        'customer_name': customer_name,
        'dish_ids': dish_ids,
        'status': order_status
    }
    mongo.db.orders.insert_one(order)
    return jsonify({'message': 'Order placed successfully'})

# Route to update the status of an order
@app.route('/orders/<order_id>', methods=['PUT'])
def update_order_status(order_id):
    # order_id = request.json['-id']
    new_status = request.json['status']
    result = mongo.db.orders.update_one(
        {'_id': ObjectId(order_id)},
        {'$set': {'status': new_status}}
    )
    if result.modified_count > 0:
        return jsonify({'message': 'Order status updated successfully'})
    else:
        return jsonify({'message': 'Order not found'})


# Route to get all orders
@app.route('/orders', methods=['GET'])
def get_all_orders():
    orders = list(mongo.db.orders.find())
    return jsonify(orders)

# Route to remove a order
@app.route('/orders/<order_id>', methods=['DELETE'])
def remove_order(order_id):
    result = mongo.db.orders.find_one_and_delete({'_id': ObjectId(order_id)})
    if result:
        return jsonify({'message': 'Order removed successfully'})
    else:
        return jsonify({'message': 'order not found'})

# Route to exit the day's operations
@app.route('/exit', methods=['GET'])
def exit_operations():
    # Perform necessary cleanup and tasks before exiting
    return jsonify({'message': 'Exiting operations'})

if __name__ == '__main__':
    app.run(debug=True)
