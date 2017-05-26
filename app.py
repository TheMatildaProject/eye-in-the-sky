import pyowm, os, sys
from flask import Flask, jsonify, request

app = Flask(__name__)
owm = pyowm.OWM(os.getenv('OWM_TOKEN'))

@app.route('/', methods=['POST'])
def weather():
    if not request.json or not 'city' in request.json:
        return jsonify({'error': 'Missing city'}), 400

    observation = owm.weather_at_place(request.json['city'])
    return jsonify({'forecast': str(observation.get_weather().get_temperature('celsius'))})

if __name__ == "__main__":
    app.run(debug=True)