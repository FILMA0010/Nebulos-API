# Sorry for my messy code. But I dont care.
from flask import Flask, jsonify, send_from_directory, render_template, render_template_string, send_file
import os
import ssl
import random

app = Flask(__name__)

@app.route('/api/images/<ordnername>')
def showimage(ordnername):
    bilder_pfad = f'APIs/ImageAPIs/{ordnername}'

    if not os.path.exists(bilder_pfad):
        return jsonify({'error': 'API not found'})

    bilder = os.listdir(bilder_pfad)
    bild_datei = random.choice(bilder)

    bild_pfad = os.path.join(bilder_pfad, bild_datei)
    return send_file(bild_pfad, mimetype='image/jpeg')

@app.route('/api/images/categories')
def zeige_kategorien():
    bilder_pfad = 'APIs/ImageAPIs'
    ordner_namen = os.listdir(bilder_pfad)
    
    return jsonify(ordner_namen)

@app.route('/api/text/categories')
def zeige_text_kategorien():
    text_pfad = 'APIs/TextAPIs'
    dateinamen = []

    for dateiname in os.listdir(text_pfad):
        if os.path.isfile(os.path.join(text_pfad, dateiname)):
            dateiname_ohne_erweiterung = os.path.splitext(dateiname)[0]
            dateinamen.append(dateiname_ohne_erweiterung)

    return jsonify(dateinamen)

@app.route('/api/text/<dateiname>')
def zeige_text(dateiname):
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

@app.route('/docs/<path:filename>')
def zeige_datei(filename):
    return send_from_directory('docs/files', filename)

@app.route('/docs/pages/<path:filename>')
def zeige_datei2(filename):
    dateiname = filename.split('.')[0]
    dateipfad = f'docs/pages/{dateiname}.html'

    with open(dateipfad, 'r') as file:
        inhalt = file.read()

    return render_template_string(inhalt)


@app.route('/docs/')
def zeige_index():
    return send_from_directory('docs/files', 'index.html')

if __name__ == '__main__':
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.load_cert_chain(certfile='/etc/letsencrypt/live/api.nebulos.pro/fullchain.pem', keyfile='/etc/letsencrypt/live/api.nebulos.pro/privkey.pem')
    app.run()
#    app.run(ssl_context=ssl_context, host='0.0.0.0', port=5000)