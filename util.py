import googlemaps
import os
from dotenv import load_dotenv

load_dotenv()
KEY = os.environ['KEY']
gmaps = googlemaps.Client(key=KEY)

#リストにいくつか緯度・経度を格納する
list = [
    "35.65858645, 139.745440057962", #東京タワー
    "35.71005425, 139.810714099926" #東京スカイツリー
]
list = ["35.6642137882687, 139.87317085663196"]

for i in list:
    results = gmaps.reverse_geocode((i), language='ja')
    add = [d.get('formatted_address') for d in results]
    print(add[1])

#=>日本、〒105-0011 東京都港区芝公園４丁目２−８
#=>日本、〒131-0045 東京都墨田区押上１丁目１−８３
