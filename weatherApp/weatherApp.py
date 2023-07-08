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



# GET all weather data
@app.route('/weather', methods=['GET'])
def get_all_weather():
    return jsonify(weather_data)

# GET weather data by ID
@app.route('/weather/<int:weather_id>', methods=['GET'])
def get_weather_by_id(weather_id):
    for data in weather_data:
        if data['id'] == weather_id:
            return jsonify(data)
    return jsonify({'message': 'Weather data not found'})

# CREATE new weather data
@app.route('/weather', methods=['POST'])
def create_weather():
    new_weather = {
        'id': len(weather_data) + 1,
        'city': request.json['city'],
        'temperature': request.json['temperature'],
        'conditions': request.json['conditions']
    }
    weather_data.append(new_weather)
    return jsonify(new_weather)

# UPDATE weather data
@app.route('/weather/<int:weather_id>', methods=['PUT'])
def update_weather(weather_id):
    for data in weather_data:
        if data['id'] == weather_id:
            data['city'] = request.json.get('city', data['city'])
            data['temperature'] = request.json.get('temperature', data['temperature'])
            data['conditions'] = request.json.get('conditions', data['conditions'])
            return jsonify(data)
    return jsonify({'message': 'Weather data not found'})

# DELETE weather data
@app.route('/weather/<int:weather_id>', methods=['DELETE'])
def delete_weather(weather_id):
    for data in weather_data:
        if data['id'] == weather_id:
            weather_data.remove(data)
            return jsonify({'message': 'Weather data deleted'})
    return jsonify({'message': 'Weather data not found'})

if __name__ == '__main__':
    app.run()

