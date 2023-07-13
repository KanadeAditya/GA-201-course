from flask import Flask, jsonify , request
import uuid

app = Flask(__name__)

db = []

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/post",methods = ["GET"])
def post():
    return jsonify(db)


@app.route("/post/<post_id>",methods = ["GET"])
def getpost(post_id):
    for items in db:
        if items["post_id"]== post_id:
            return items
    return jsonify({"message":"Post not found"})
        
@app.route("/post/<post_id>",methods = ["DELETE"])
def deletepost(post_id):
    for items in db:
        if items["post_id"]== post_id:
            db.remove(items)
            return jsonify({"message":"Post removed successfully"})
    return jsonify({"message":"Post not found"})
        


@app.route("/post",methods = ["POST"])
def getposts():
    newpost = request.get_json()
    newpost["post_id"] = str(uuid.uuid4())
    db.append(newpost)
    return jsonify({"message":"Post has been added"})

if(__name__=="__main__"):
    app.run(debug=True)