from models import db, Artist

def get_all_artists():
    return Artist.query.all()