// ボタンを押した時の処理
document.getElementById("btn").onclick = function(){
    // 位置情報を取得する
    navigator.geolocation.getCurrentPosition(successCallback, errorCallback);
};


// 取得に失敗した場合の処理
function errorCallback(error){
    alert("位置情報が取得できませんでした");
};

function successCallback(position) {
    var latitude = position.coords.latitude;
    var longitude = position.coords.longitude;

    // APIにリクエストを送信
    fetch('https://location-alart-e86815bc444e.herokuapp.com/convert', {
    // fetch('http://127.0.0.1:5000/convert', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ latitude: latitude, longitude: longitude }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("address").innerHTML = data.address;
     })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function getLocationAndUpdate() {
    console.log("関数が呼び出されました: ", new Date().toLocaleTimeString());
    if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition(function(position) {
            var lat = position.coords.latitude;
            var lng = position.coords.longitude;
            console.log("緯度: " + lat + ", 経度: " + lng);
            
            // ここでサーバーに位置情報を送信する
            fetch('https://location-alart-e86815bc444e.herokuapp.com/convert', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ latitude: lat, longitude: lng }),
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
            })
            .catch((error) => {
                console.error('Error:', error);
            });

        }, function(error) {
            console.error("エラーコード: " + error.code + " - " + error.message);
        }, {
            enableHighAccuracy: true,
            timeout: 10000,
            maximumAge: 0
        });
    } else {
        console.error("このブラウザでは位置情報が利用できません。");
    }
}

// 1分ごとにgetLocationAndUpdate関数を実行
setInterval(getLocationAndUpdate, 3600000/60);

// ページロード時にも一度実行
getLocationAndUpdate();

