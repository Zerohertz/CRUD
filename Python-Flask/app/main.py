import os
from datetime import datetime

from flask import Flask, abort, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"""postgresql://{os.environ["POSTGRES_USER"]}:{os.environ["POSTGRES_PASSWORD"]}@{os.environ["POSTGRES_HOST"]}:{os.environ["POSTGRES_PORT"]}/{os.environ["POSTGRES_DB"]}"""
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=True, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }


def create_tables():
    with app.app_context():
        db.create_all()


@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    if not data or not all(k in data for k in ("username", "email", "password")):
        abort(400, description="Bad Request: Missing required fields.")

    try:
        new_user = User(
            username=data["username"], email=data["email"], password=data["password"]
        )
        db.session.add(new_user)
        db.session.commit()

        return jsonify(new_user.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        abort(409, description="Conflict: Username or email already exists.")


@app.route("/users", methods=["GET"])
def get_all_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200


@app.route("/users/<int:id>", methods=["GET"])
def get_user_by_id(id):
    user = User.query.get(id)
    if not user:
        abort(404, description="Not Found: User does not exist.")
    return jsonify(user.to_dict()), 200


@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    user = User.query.get(id)
    if not user:
        abort(404, description="Not Found: User does not exist.")

    data = request.json
    if not data:
        abort(400, description="Bad Request: Missing required fields.")

    if "username" in data:
        user.username = data["username"]
    if "email" in data:
        user.email = data["email"]

    db.session.commit()
    return jsonify(user.to_dict()), 200


@app.route("/users/<int:id>", methods=["PATCH"])
def partially_update_user(id):
    user = User.query.get(id)
    if not user:
        abort(404, description="Not Found: User does not exist.")

    data = request.json
    if not data:
        abort(400, description="Bad Request: Missing required fields.")

    if "username" in data:
        user.username = data["username"]
    if "email" in data:
        user.email = data["email"]

    db.session.commit()
    return jsonify(user.to_dict()), 200


@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        abort(404, description="Not Found: User does not exist.")

    db.session.delete(user)
    db.session.commit()
    return "", 204


if __name__ == "__main__":
    create_tables()
