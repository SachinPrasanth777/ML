from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URI")
db = SQLAlchemy(app)


class user(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.string(80), unique=True, nullable=False)
    email = db.Column(db.string(120), unique=True, nullable=False)

    def json(self):
        return {"id": id, "username": self.username, "email": self.email}


db.create_all()


@app.get("/")
def home():
    return "Hello World!"


@app.route("/test", methods=["GET"])
def test():
    return make_response(jsonify({"message": "Test Route"}, 200))
