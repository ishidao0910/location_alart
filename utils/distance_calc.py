import math
import os
from dotenv import load_dotenv

load_dotenv()
REGISTERD_LAT = float(os.environ['REGISTERED_LAT'])
REGISTERD_LNG = float(os.environ['REGISTERED_LNG'])

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0 # 地球の半径 (km)

    # 緯度経度をラジアンに変換
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # ハーヴァサイン公式
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c

    return distance

input_lat = 35.666738
input_lng = 139.895827

distance = haversine(REGISTERD_LAT, REGISTERD_LNG, input_lat, input_lng)

if distance > 1:
    print("指定された地点は半径1km以上離れています。")
else:
    print("指定された地点は半径1km以内です。")
