import pyowm
import json
from flask import Flask

app = Flask(__name__)
owm = pyowm.OWM('cc9b14c75920b2df47b3d8b6d6cce6f2')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello(path):
    observation = owm.weather_at_place(path)
    return str(observation.get_weather().get_temperature('celsius'))

if __name__ == "__main__":
    app.run()