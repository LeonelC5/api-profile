from flask import Flask, jsonify, request, abort, jsonify, url_for, redirect
from flask_cors import CORS
from uuid import uuid4

app = Flask(__name__)
app.secret_key = "my_secret_key"

CORS(app, resources={r"/": {"origins": ""}}, supports_credentials=True)

# In-memory storage for profiles
profiles = {}
last_id = max(profiles.keys()) if profiles else 0

@app.route("/profile", methods=["GET"])
def get_profiles():
    return jsonify(list(profiles.values()))

@app.route("/profile/<int:id>", methods=["GET"])
def get_profile(id):
    if id in profiles:
        return jsonify(profiles[id])
    else:
        return jsonify({"error": "Perfil no encontrado"}), 404
    
@app.route("/profile", methods=["POST"])
def create_profile():
    global last_id
    data = request.json
    if "name" in data and "last_name" in data and "age" in data:
        last_id += 1
        new_profile = {
            "id": last_id,
            "name": data["name"],
            "last_name": data["last_name"],
            "age": data["age"]
        }
        profiles[last_id] = new_profile
        return jsonify({"message": "Perfil creado exitosamente", "profile": new_profile}), 201
    else:
        return jsonify({"error": "Faltan datos en la solicitud"}), 400

@app.route("/profile/<int:id>", methods=["PUT"])
def update_profile(id):
    if id in profiles:
        data = request.json
        if "name" in data:
            profiles[id]["name"] = data["name"]
        if "last_name" in data:
            profiles[id]["last_name"] = data["last_name"]
        if "age" in data:
            profiles[id]["age"] = data["age"]
        return jsonify({"message": "Perfil actualizado exitosamente", "profile": profiles[id]}), 200
    else:
        return jsonify({"error": "Perfil no encontrado"}), 404

@app.route("/profile/<int:id>", methods=["DELETE"])
def delete_profile(id):
    if id in profiles:
        del profiles[id]
        return jsonify({"message": "Perfil eliminado exitosamente"}), 200
    else:
        return jsonify({"error": "Perfil no encontrado"}), 404
    
if __name__ == '__main__':
    app.run(port=5500, debug=True)
