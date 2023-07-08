from flask import Flask, jsonify

app = Flask(__name__)


weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}


@app.route('/weather/<city>')
def weather(city):
    for data in weather_data:
        if data['city'].lower() == city.lower():
            return jsonify(data)
    return jsonify({'message': 'Weather data not found for the given city'})

if __name__ == '__main__':
    app.run()

