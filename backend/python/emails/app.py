from flask import Flask, request, jsonify
from routes import emails_blueprint
from models import db, AddEmail, init_app
from flask_migrate import Migrate
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app
app.config['SECRET_KEY'] = 'z0ImlcAWqWik9PVsmUtg7g'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///email.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(emails_blueprint)

init_app(app)

migrate = Migrate(app, db)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
