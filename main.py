# Copyright Nebulos Production 2024
# This code is really messy i know. I am also normally a Javascript developer.
# It turned out pretty good for that.
from flask import Flask, jsonify, send_from_directory, render_template, render_template_string, send_file, redirect, request
import os
import ssl
import random
import logging
import json
import requests
from flask_cors import CORS

# Define App
app = Flask(__name__)
CORS(app)

#Force HTTPS
@app.before_request
def redirect_to_https():
    if request.headers.get('X-Forwarded-Proto') == 'http':
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=301)

#  _____ ______   ____  ______  _____
# / ___/|      | /    ||      |/ ___/
#(   \_ |      ||  o  ||      (   \_ 
# \__  ||_|  |_||     ||_|  |_|\__  |
# /  \ |  |  |  |  _  |  |  |  /  \ |
# \    |  |  |  |  |  |  |  |  \    |
#  \___|  |__|  |__|__|  |__|   \___|

def count_files(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
        count += len(files)
    return count

def count_folders(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
        count += len(dirs)
    return count


textapi_count = count_files('APIs/TextAPIs')

imageapi_count = count_folders('APIs/ImageAPIs')

endpoints = textapi_count + imageapi_count + 9

with open('stats.json', 'r') as file:
    data = json.load(file)

data['endpoints'] = endpoints

with open('stats.json', 'w') as file:
    json.dump(data, file)

# Stats Route
@app.route('/api/stats', methods=['GET'])
def get_stats():
    with open('stats.json', 'r') as file:
        data = json.load(file)
        reqs = data['requests']

    reqs += 1
    data['requests'] = reqs
    with open('stats.json', 'w') as file:
        json.dump(data, file)
    with open('stats.json', 'r') as file:
        data = json.load(file)
        requests = data['requests']
        endpoints = data['endpoints']

    stats = {
        'requests': requests,
        'endpoints': endpoints
    }

    return jsonify(stats)

#  ___ ___   ____  ____  ____  
# |   |   | /    ||    ||    \ 
# | _   _ ||  o  | |  | |  _  |
# |  \_/  ||     | |  | |  |  |
# |   |   ||  _  | |  | |  |  |
# |   |   ||  |  | |  | |  |  |
# |___|___||__|__||____||__|__|

# Default route
@app.route('/')
def zeige_index():
    return send_from_directory('docs/files', 'index.html')

# Files
@app.route('/docs/<path:filename>')
def showfile(filename):
    return send_from_directory('docs/files', filename)

@app.route('/docs/pages/<path:filename>')
def showfile2(filename):
    filename2 = filename.split('.')[0]
    path = f'docs/pages/{filename2}.html'

    with open(path, 'r') as file:
        inhalt = file.read()

    return render_template_string(inhalt)

#    __   ____  ______    ___   ____   ___   ____   ____    ___  _____
#   /  ] /    ||      |  /  _] /    | /   \ |    \ |    |  /  _]/ ___/
#  /  / |  o  ||      | /  [_ |   __||     ||  D  ) |  |  /  [_(   \_ 
# /  /  |     ||_|  |_||    _]|  |  ||  O  ||    /  |  | |    _]\__  |
#/   \_ |  _  |  |  |  |   [_ |  |_ ||     ||    \  |  | |   [_ /  \ |
#\     ||  |  |  |  |  |     ||     ||     ||  .  \ |  | |     |\    |
# \____||__|__|  |__|  |_____||___,_| \___/ |__|\_||____||_____| \___|


# All Endpoints                                                                 
@app.route('/api/endpoints')
def get_endpoints():
    with open('stats.json', 'r') as file:
        data = json.load(file)
        reqs = data['requests']

    reqs += 1
    data['requests'] = reqs
    with open('stats.json', 'w') as file:
        json.dump(data, file)
    endpoints = [
        "api/endpoints",
        "api/text/geek-jokes",
        "api/text/usleess-facts",
        "api/text/wouldyourather",
        "api/text/categories",
        "api/images/dogs",
        "api/images/aghpb",
        "api/images/categories",
        "api/roblox/users/[id]",
        "api/roblox/groups/[id]",
        "api/roblox/categories",
        "api/minecraft/server/java/{adress[:port]}",
        "api/minecraft/server/bedrock/{adress[]:port]}",
        "api/minecraft/uuid/{uuid}"
    ]
    return jsonify(endpoints)

# Roblox API Categories
@app.route('/api/roblox/categories')
def get_categories():
    with open('stats.json', 'r') as file:
        data = json.load(file)
        reqs = data['requests']

    reqs += 1
    data['requests'] = reqs
    with open('stats.json', 'w') as file:
        json.dump(data, file)
    categories = [
        "groups",
        "users"
    ]
    return jsonify(categories)

# Minecraft API Categories
@app.route('/api/minecraft/categories')
def get_categories2():
    with open('stats.json', 'r') as file:
        data = json.load(file)
        reqs = data['requests']

    reqs += 1
    data['requests'] = reqs
    with open('stats.json', 'w') as file:
        json.dump(data, file)
    categories = [
        "server/bedrock",
        "server/java",
        "uuid"
    ]
    return jsonify(categories)

# Text API Categories
@app.route('/api/text/categories')
def zeige_text_kategorien():
    with open('stats.json', 'r') as file:
        data = json.load(file)
        reqs = data['requests']

    reqs += 1
    data['requests'] = reqs
    with open('stats.json', 'w') as file:
        json.dump(data, file)
    text_pfad = 'APIs/TextAPIs'
    dateinamen = []

    for dateiname in os.listdir(text_pfad):
        if os.path.isfile(os.path.join(text_pfad, dateiname)):
            dateiname_ohne_erweiterung = os.path.splitext(dateiname)[0]
            dateinamen.append(dateiname_ohne_erweiterung)

    return jsonify(dateinamen)

# Image API Categories
@app.route('/api/images/categories')
def zeige_kategorien():
    with open('stats.json', 'r') as file:
        data = json.load(file)
        reqs = data['requests']

    reqs += 1
    data['requests'] = reqs
    with open('stats.json', 'w') as file:
        json.dump(data, file)

    bilder_pfad = 'APIs/ImageAPIs'
    ordner_namen = os.listdir(bilder_pfad)
    
    return jsonify(ordner_namen)

#  ____  ____ ____ _____
# /    ||    \    / ___/
#|  o  ||  o  )  (   \_ 
#|     ||   _/|  |\__  |
#|  _  ||  |  |  |/  \ |
#|  |  ||  |  |  |\    |
#|__|__||__| |____|\___|

# Minecraft Java API
@app.route('/api/minecraft/server/java/<adress>', methods=['GET'])
def get_jserver_info(adress):
    with open('stats.json', 'r') as file:
        data = json.load(file)
        reqs = data['requests']

    reqs += 1
    data['requests'] = reqs
    with open('stats.json', 'w') as file:
        json.dump(data, file)
    response = requests.get(f'https://api.mcsrvstat.us/3/{adress}')
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to fetch server information'}), response.status_code

# Minecraft Bedrock API
@app.route('/api/minecraft/server/bedrock/<adress>', methods=['GET'])
def get_bserver_info(adress):
    with open('stats.json', 'r') as file:
        data = json.load(file)
        reqs = data['requests']

    reqs += 1
    data['requests'] = reqs
    with open('stats.json', 'w') as file:
        json.dump(data, file)
    response = requests.get(f'https://api.mcsrvstat.us/bedrock/3/{adress}')
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to fetch server information'}), response.status_code

# Minecraft UUID API
@app.route('/api/minecraft/uuid/<uuid>', methods=['GET'])
def get_uuid_info(uuid):
    with open('stats.json', 'r') as file:
        data = json.load(file)
        reqs = data['requests']

    reqs += 1
    data['requests'] = reqs
    with open('stats.json', 'w') as file:
        json.dump(data, file)
    response = requests.get(f'https://api.minetools.eu/profile/{uuid}')
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to fetch uuid information'}), response.status_code

# Roblox Group API
@app.route('/api/roblox/groups/<group_id>')
def get_group_info(group_id):
    with open('stats.json', 'r') as file:
        data = json.load(file)
        reqs = data['requests']

    reqs += 1
    data['requests'] = reqs
    with open('stats.json', 'w') as file:
        json.dump(data, file)
    import requests
    response = requests.get(f'https://groups.roblox.com/v2/groups?groupIds={group_id}')
    group_data = response.json()['data'][0]

    group_info = {
        'name': group_data['name'],
        'description': group_data['description'],
        'ownerID': group_data['owner']['id'],
        'groupID': group_data['id'],
        'createdAt': group_data['created'],
        'verified': group_data['hasVerifiedBadge']
    }

    return user_info

# Roblox User API
@app.route('/api/roblox/users/<user_id>')
def get_user_info(user_id):
    import requests
    response = requests.get(f'https://users.roblox.com/v1/users/{user_id}')
    user_data = response.json()
    with open('stats.json', 'r') as file:
        data = json.load(file)
        reqs = data['requests']

    reqs += 1
    data['requests'] = reqs
    with open('stats.json', 'w') as file:
        json.dump(data, file)
    user_info = {
        'name': user_data['name'],
        'displayName': user_data['displayName'],
        'description': user_data['description'],
        'createdAt': user_data['created'],
        'id': user_data['id'],
        'verified': user_data['hasVerifiedBadge'],
        'externalAppDisplayName': user_data['externalAppDisplayName']
    }

    return user_info

# Image API
@app.route('/api/images/<ordnername>')
def showimage(ordnername):
    with open('stats.json', 'r') as file:
        data = json.load(file)
        reqs = data['requests']

    reqs += 1
    data['requests'] = reqs
    with open('stats.json', 'w') as file:
        json.dump(data, file)
    bilder_pfad = f'APIs/ImageAPIs/{ordnername}'

    if not os.path.exists(bilder_pfad):
        return jsonify({'error': 'API not found'})

    bilder = os.listdir(bilder_pfad)
    bild_datei = random.choice(bilder)

    bild_pfad = os.path.join(bilder_pfad, bild_datei)
    return send_file(bild_pfad, mimetype='image/jpeg')

# Text API
@app.route('/api/text/<dateiname>')
def zeige_text(dateiname):
    with open('stats.json', 'r') as file:
        data = json.load(file)
        reqs = data['requests']

    reqs += 1
    data['requests'] = reqs
    with open('stats.json', 'w') as file:
        json.dump(data, file)
    text_pfad = f'APIs/TextAPIs/{dateiname}.txt'
    zeilen = []

    try:
        with open(text_pfad, 'r') as file:
            zeilen = file.readlines()
            zufaellige_zeile = random.choice(zeilen)
            zeilennummer = zeilen.index(zufaellige_zeile) + 1
    except FileNotFoundError:
        return jsonify({'error': 'API not found'})
    except Exception as e:
        return jsonify({'error': str(e)})

    return jsonify({'message': zufaellige_zeile.strip()})
#  _____ ______   ____  ____  ______ 
# / ___/|      | /    ||    \|      |
#(   \_ |      ||  o  ||  D  )      |
# \__  ||_|  |_||     ||    /|_|  |_|
# /  \ |  |  |  |  _  ||    \  |  |  
# \    |  |  |  |  |  ||  .  \ |  |  
#  \___|  |__|  |__|__||__|\_| |__|  

if __name__ == '__main__':
#    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH) # Required for SSL
#    ssl_context.load_cert_chain(certfile='fullchain.pem', keyfile='privkey.pem') # Required for SSL
    app.run(port='31000', host='0.0.0.0') # Without SSL
#    app.run(ssl_context=ssl_context, host='0.0.0.0', port=3000) # Required for SSL 38
