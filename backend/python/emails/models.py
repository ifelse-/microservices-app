from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app):
    db.app = app
    db.init_app(app)


class AddEmail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticketId = db.Column(db.Integer, unique=True)
    userId = db.Column(db.Integer, unique=True)

    def __repr__(self):
        return f'<email {self.id} {self.userId}  >'

    def serialize(self):
        return {
            'id': self.id,
            'ticketId': self.ticketId,
            'userId': self.userId
        }
