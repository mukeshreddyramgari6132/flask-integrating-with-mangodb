import pymongo
from flask import Flask,jsonify

app = Flask(__name__)

mongodb_client = pymongo(app, uri="mongodb://localhost:27017/todo_db")
db = mongodb_client.db

app.config["MONGO_URI"] = "mongodb://localhost:27017/todo_db"
mongodb_client = pymongo(app)
db = mongodb_client.db
######
@app.route("/add_one")
def add_one():
    db.todos.insert_one({'title': "todo title", 'body': "todo body"})
    return jsonify(message="success")

if __name__=="__main__":
    app.run(debug=True)