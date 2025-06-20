
import requests
from app.extensions import db
from app.models.album import Album

def fetch_and_store_albums():
    url = "https://jsonplaceholder.typicode.com/albums"
    response = requests.get(url)
    if response.status_code == 200:
        albums_data = response.json()
        for item in albums_data:
            album = Album.query.get(item['id'])
            if not album:
                db.session.add(Album(id=item['id'], title=item['title']))
        db.session.commit()
        return {"message": "Albums fetched and stored successfully"}
    else:
        raise Exception("Failed to fetch albums")

def get_albums(query=None):
    if query:
        return Album.query.filter(Album.title.ilike(f"%{query}%")).all()
    return Album.query.all()

def get_album(album_id):
    return Album.query.get_or_404(album_id)

def create_album(album):
    db.session.add(album)
    db.session.commit()
    return album

def update_album(album_id, data):
    album = Album.query.get_or_404(album_id)
    for key, value in data.items():
        setattr(album, key, value)
    db.session.commit()
    return album

def delete_album(album_id):
    album = Album.query.get_or_404(album_id)
    db.session.delete(album)
    db.session.commit()
