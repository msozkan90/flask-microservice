
from flask import Blueprint, request, jsonify
from app.schemas.album import AlbumSchema
from app.services.album_service import (
    fetch_and_store_albums,
    get_albums,
    get_album,
    create_album,
    update_album,
    delete_album
)
from app.services.auth_service import token_required

album_bp = Blueprint("albums", __name__)
album_schema = AlbumSchema()
albums_schema = AlbumSchema(many=True)


@album_bp.route("/albums/fetch", methods=["POST"])
@token_required
def fetch_albums(user_id):
    result = fetch_and_store_albums()
    return jsonify(result)

@album_bp.route("/albums", methods=["GET"])
@token_required
def list_albums(user_id):
    query = request.args.get("query")
    albums = get_albums(query)
    return jsonify(albums_schema.dump(albums))


@album_bp.route("/albums/<int:album_id>", methods=["GET"])
@token_required
def retrieve_album(user_id, album_id):
    a = get_album(album_id)
    return jsonify({"id": a.id, "title": a.title})

@album_bp.route("/albums", methods=["POST"])
@token_required
def create(user_id):
    album = album_schema.load(request.json)
    a = create_album(album)
    return jsonify(album_schema.dump(a)), 201


@album_bp.route("/albums/<int:album_id>", methods=["PUT"])
@token_required
def update(user_id, album_id):
    data = request.json
    a = update_album(album_id, data)
    return jsonify(album_schema.dump(a))

@album_bp.route("/albums/<int:album_id>", methods=["DELETE"])
@token_required
def delete(user_id, album_id):  
    delete_album(album_id)
    return jsonify({"message": "Album deleted successfully"})
