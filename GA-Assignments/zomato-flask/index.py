from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Initialize dishes and orders as empty lists
dishes = []
orders = []
order_id_counter = 1

# Load dishes and orders from file if it exists
def load_data():
    global dishes, orders, order_id_counter
    try:
        with open('data.pickle', 'rb') as file:
            data = pickle.load(file)
            dishes = data['dishes']
            orders = data['orders']
            order_id_counter = data['order_id_counter']
    except FileNotFoundError:
        # If the file doesn't exist, initialize with sample data
        dishes = [
            {"id": 1, "name": "Pasta", "price": 10.99, "availability": True},
            {"id": 2, "name": "Pizza", "price": 15.99, "availability": True},
            {"id": 3, "name": "Burger", "price": 8.99, "availability": False}
        ]
        orders = []
        order_id_counter = 1

# Update dishes and orders file on application exit
def save_data():
    data = {'dishes': dishes, 'orders': orders, 'order_id_counter': order_id_counter}
    with open('data.pickle', 'wb') as file:
        pickle.dump(data, file)


@app.route('/dishes', methods=['GET'])
def get_dishes():
    return jsonify(dishes)

# Flask route for adding a new dish to the menu
@app.route('/dishes', methods=['POST'])
def add_dish():
    # Parse dish data from the request
    dish_data = request.json
    # Generate a new ID for the dish
    dish_data['id'] = len(dishes) + 1
    # Add the dish to the menu
    dishes.append(dish_data)
    # Save the updated data
    save_data()
    return jsonify({"message": "Dish added successfully"})

# Flask route for removing a dish from the menu
@app.route('/dishes/<int:dish_id>', methods=['DELETE'])
def remove_dish(dish_id):
    # Find the dish by ID
    dish = next((d for d in dishes if d['id'] == dish_id), None)
    if dish:
        # Remove the dish from the menu
        dishes.remove(dish)
        # Save the updated data
        save_data()
        return jsonify({"message": "Dish removed successfully"})
    else:
        return jsonify({"message": "Dish not found"})

# Flask route for updating the availability of a dish
@app.route('/dishes/<int:dish_id>', methods=['PUT'])
def update_dish_availability(dish_id):
    # Find the dish by ID
    dish = next((d for d in dishes if d['id'] == dish_id), None)
    if dish:
        # Parse availability data from the request
        availability = request.json.get('availability')
        if availability is not None:
            # Update the availability of the dish
            dish['availability'] = availability
            # Save the updated data
            save_data()
            return jsonify({"message": "Dish availability updated successfully"})
        else:
            return jsonify({"message": "Invalid request"})
    else:
        return jsonify({"message": "Dish not found"})

# Flask route for taking a new order
@app.route('/orders', methods=['POST'])
def place_order():
    # Parse order data from the request
    order_data = request.json
    customer_name = order_data.get('customer_name')
    dish_ids = order_data.get('dish_ids')
    print(customer_name,dish_ids)
    if customer_name and dish_ids:
        # Check if all dishes are available
        available_dishes = []
        # if len(dishes):
        for d in dishes:
            if d['id'] in dish_ids and d['availability']:
                available_dishes.append(d)
        if len(available_dishes) == len(dish_ids):
            # Generate a unique order ID
            global order_id_counter
            order_id = order_id_counter
            order_id_counter += 1
            # Create a new order
            order = {"id": order_id, "customer_name": customer_name, "dish_ids": dish_ids, "status": "received"}
            orders.append(order)
            # Save the updated data
            save_data()
            return jsonify({"message": "Order placed successfully", "order_id": 1})
        else:
            return jsonify({"message":"Some dishes are not available"})
    else:
        return jsonify({"message": "Invalid request"})

# Flask route for updating the status of an order
@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order_status(order_id):
    # Find the order by ID
    order = next((o for o in orders if o['id'] == order_id), None)
    if order:
        # Parse status data from the request
        status = request.json.get('status')
        if status:
            # Update the status of the order
            order['status'] = status
            # Save the updated data
            save_data()
            return jsonify({"message": "Order status updated successfully"})
        else:
            return jsonify({"message": "Invalid request"})
    else:
        return jsonify({"message": "Order not found"})

# Flask route for reviewing all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

# Flask route for handling the exit option
@app.route('/exit', methods=['GET'])
def exit_app():
    # Save the data and exit the application
    save_data()
    return jsonify({"message": "Application exited"})

# Load data on application startup
load_data()

# Run the Flask application
if __name__ == '__main__':
    app.run(port=4040)
