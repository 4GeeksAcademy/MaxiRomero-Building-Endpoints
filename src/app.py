"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/people', methods=['GET'])
def getPeople():
    people = People.query.all()
    serialized_people = [p.serialize() for p in people]


    return jsonify(serialized_people), 200

@app.route('/people', methods=['POST'])
def create_person():
    body = request.get_json()
    new_person = People(name = body['name'], description = body['description'])
    db.session.add(new_person)
    db.session.commit()
    return jsonify({'person': new_person.serialize()}), 200

### DELETE PLANET
@app.route('/people/<int:people_id>', methods= ['DELETE'])
def deletePeople(people_id):
    person = People.query.get(people_id)
    db.session.delete(person)
    db.session.commit()

    return jsonify(person.serialize())

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
