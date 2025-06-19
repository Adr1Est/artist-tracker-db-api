from flask import Flask, jsonify, request
from models import db, User, Artist
from db_utils import get_all_artists
from config import Config
from data import registrar_artistas
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
CORS(app)

@app.route('/', methods=['GET'])
def hello():
    saludo = { "200": "API de Artist Tracker"}
    return jsonify(saludo), 200

@app.route('/artists', methods=['GET'])
def get_artists():
    artists_data = get_all_artists()
    if not artists_data:
        return jsonify({"info": "Sin datos de artistas."}), 200
    
    return jsonify([artist.serialize() for artist in artists_data]), 200
        
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        if not Artist.query.first():
            lista_artistas = registrar_artistas()
            db.session.add_all(lista_artistas)
            db.session.commit()
    app.run(debug=True)