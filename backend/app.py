from flask import Flask, request, jsonify
import googlemaps
import os

from flask import Flask, request, jsonify
from flask_cors import CORS
import googlemaps
import os

app = Flask(__name__)
CORS(app)

@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    latitude = data['latitude']
    longitude = data['longitude']
    gmaps = googlemaps.Client(key=os.environ['KEY'])

    results = gmaps.reverse_geocode((latitude, longitude), language='ja')
    address = results[0].get('formatted_address') if results else '住所が見つかりません'

    return jsonify({'address': address})

if __name__ == '__main__':
    app.run(debug=True)
