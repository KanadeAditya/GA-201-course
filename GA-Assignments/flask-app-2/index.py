from flask import Flask, request

app = Flask(__name__)

data = []


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # key = request.form['key']
        # value = request.form['value']
        # data[key] = value
        data.append(request.json)
        return f"Entry created: {request.json}"
    return "Create route"


@app.route('/read')
def read():
    return str(data)


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        key = request.form['key']
        value = request.form['value']
        if key in data:
            data[key] = value
            return f"Entry updated: {key} - {value}"
        return f"Entry not found: {key}"
    return "Update route"


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        key = request.form['key']
        if key in data:
            del data[key]
            return f"Entry deleted: {key}"
        return f"Entry not found: {key}"
    return "Delete route"


if __name__ == '__main__':
    app.run(debug=True)
