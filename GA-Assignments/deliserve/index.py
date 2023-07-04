from flask import Flask, render_template, request, jsonify, redirect, url_for
import pickle

app = Flask(__name__)

# Load the dishes from a pickle file
def load_dishes():
    try:
        with open('dishes.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

# Save the dishes to a pickle file
def save_dishes(dishes):
    with open('dishes.pkl', 'wb') as file:
        pickle.dump(dishes, file)

# Home page route
@app.route('/')
def home():
    return render_template('menu.html', dishes=load_dishes())

# Add a new dish route
@app.route('/add_dish', methods=['POST'])
def add_dish():
    dish_id = request.form.get('dish_id')
    dish_name = request.form.get('dish_name')
    price = request.form.get('price')
    availability = request.form.get('availability')

    # Create a new dish object
    dish = {
        'dish_id': dish_id,
        'dish_name': dish_name,
        'price': price,
        'availability': availability
    }

    dishes = load_dishes()
    dishes.append(dish)
    save_dishes(dishes)

    return redirect(url_for('home'))

# Update dish availability route
@app.route('/update_availability/<dish_id>', methods=['POST','GET'])
def update_availability(dish_id):
    # dish_id = request.form.get('dish_id')

    dishes = load_dishes()
    for dish in dishes:
        if dish['dish_id'] == dish_id:
            # print(dish)
            if dish['availability'] == 'yes':
                dish['availability'] = 'no'
            else:
                dish['availability'] ='yes'
            break

    save_dishes(dishes)

    return redirect(url_for('home'))

# Delete dish route
@app.route('/delete-dish/<dish_id>', methods=['POST','GET'])
def delete_dish(dish_id):
    # dish_id = request.json.get('dish_id')

    dishes = load_dishes()
    dishes_updated = []
    for dish in dishes:
        if dish['dish_id'] !=  dish_id:
            dishes_updated.append(dish)

    dishes = dishes_updated
    print(dishes)
    save_dishes(dishes)

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
