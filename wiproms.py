import flask
import flask_sqlalchemy
import flask_restless

app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = flask_sqlalchemy.SQLAlchemy(app)


class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group = db.Column(db.Integer)
    description = db.Column(db.String(128))


class Branches(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)


db.create_all()

manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)

manager.create_api(Events, methods=['GET', 'POST'])
manager.create_api(Branches, methods=['GET'])

if __name__ == '__main__':
    app.run(debug=True)

# curl -i -H "Content-Type: application/json" -X POST -d '{"group": 5, "description": "just testing"}' http://localhost:5000/api/events
# curl -i http://localhost:5000/api/events
# curl -i http://localhost:5000/api/events/1