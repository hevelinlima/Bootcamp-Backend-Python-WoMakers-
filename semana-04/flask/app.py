from flask import Flask, render_template
import json
import urllib.request
import certifi

##O certifi e a mudança dentro da variável response foram necessários para contornar um erro, sem eles o código retornava um erro de certificação ssl.

app = Flask(__name__)


# Endpoint: characters
@app.route("/")
def get_list_characters_page():
    url = "http://rickandmortyapi.com/api/character"
    response = urllib.request.urlopen(url, cafile=certifi.where())
    data = response.read()
    dicionario = json.loads(data)

    return render_template("characters.html", characters=dicionario["results"])


@app.route("/profile/<id>")
def get_profile(id):
    url = "http://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url, cafile=certifi.where())
    data = response.read()
    dicionario = json.loads(data)

    # Pegar o id da localização do personagen dentro da API
    urlLocation = dicionario["location"]["url"]
    parts = urlLocation.split("/")
    dicionario["location"]["id"] = parts[-1]

    # Pegar o id da origem do persongem dentro da API
    urlOrigin = dicionario["origin"]["url"]
    if urlOrigin:
        parts = urlOrigin.split("/")
        dicionario["origin"]["id"] = parts[-1]
    else:
        dicionario["origin"]["id"] = None

    # Pegar o id dos episódios que o personagem aperece dentro da API
    urlEpisode = dicionario["episode"]
    episode_ids = []

    for episode in urlEpisode:
        parts = episode.split("/")
        episode_id = parts[-1]
        episode_ids.append(episode_id)

    dicionario["episode_ids"] = episode_ids

    return render_template("profile.html", profile=dicionario)


@app.route("/lista")
def get_list_characters():
    url = "http://rickandmortyapi.com/api/character"
    response = urllib.request.urlopen(url, cafile=certifi.where())
    characters = response.read()
    dicionario = json.loads(characters)

    characters = []

    for character_in_dic in dicionario["results"]:
        character = {
            "name": character_in_dic["name"],
            "status": character_in_dic["status"],
            "id": character_in_dic["id"],
        }

        characters.append(character)

    return {"characters": characters}


# Endpoint: locations
@app.route("/locations")
def get_list_locations_page():
    url = "http://rickandmortyapi.com/api/location"
    response = urllib.request.urlopen(url, cafile=certifi.where())
    data = response.read()
    dicionario = json.loads(data)

    return render_template("locations.html", locations=dicionario["results"])


@app.route("/location/<id>")
def get_location(id):
    url = "http://rickandmortyapi.com/api/location/" + id
    response = urllib.request.urlopen(url, cafile=certifi.where())
    data = response.read()
    dicionario = json.loads(data)

    urlResidents = dicionario["residents"]
    resident_ids = []

    for resident in urlResidents:
        parts = resident.split("/")
        resident_id = parts[-1]
        resident_ids.append(resident_id)

    dicionario["resident_ids"] = resident_ids

    return render_template("location.html", location=dicionario)


# Endpoint: episodes
@app.route("/episodes")
def get_list_episodes_page():
    url = "http://rickandmortyapi.com/api/episode"
    response = urllib.request.urlopen(url, cafile=certifi.where())
    data = response.read()
    dicionario = json.loads(data)

    return render_template("episodes.html", episodes=dicionario["results"])


@app.route("/episode/<id>")
def get_episode(id):
    url = "http://rickandmortyapi.com/api/episode/" + id
    response = urllib.request.urlopen(url, cafile=certifi.where())
    data = response.read()
    dicionario = json.loads(data)

    urlCharacters = dicionario["characters"]
    character_ids = []

    for character in urlCharacters:
        parts = character.split("/")
        character_id = parts[-1]
        character_ids.append(character_id)

    dicionario["character_ids"] = character_ids

    return render_template("episode.html", episode=dicionario)


if __name__ == "__main__":
    app.run(debug=False)
