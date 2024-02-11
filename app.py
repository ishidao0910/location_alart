from flask import Flask, request, jsonify
from flask_cors import CORS
import googlemaps
import os
from dotenv import load_dotenv
from utils.distance_calc import haversine
from utils.line_message_api import send_line_message

load_dotenv()
REGISTERD_LAT = float(os.environ['REGISTERED_LAT'])
REGISTERD_LNG = float(os.environ['REGISTERED_LNG'])
LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
MY_LINE_USER_ID = os.environ["MY_LINE_USER_ID"]
GOOGLE_MAPS_API_KEY = os.environ['GOOGLE_MAPS_API_KEY']

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Home page'

@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    latitude, longitude = data['latitude'], data['longitude']
    gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)
    distance = haversine(REGISTERD_LAT, REGISTERD_LNG, latitude, longitude)

    if distance <= 1:
        return jsonify({'address': "1km以内", 'message': "message_text"})
    else:
        results = gmaps.reverse_geocode((latitude, longitude), language='ja')
        address = results[0].get('formatted_address') if results else '住所が見つかりません'
        message_text = (
            f"奴の現在地は、{address}\n"
             "ここは登録地点から半径1km以上離れているよ。"
        )
        send_line_message(LINE_CHANNEL_ACCESS_TOKEN, MY_LINE_USER_ID, message_text)
        return jsonify({'address': address, 'message': message_text})

if __name__ == '__main__':
    app.run(debug=True)
