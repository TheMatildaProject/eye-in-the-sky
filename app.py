import pyowm, sys
from flask import Flask

app = Flask(__name__)
owm = pyowm.OWM(sys.argv[1])

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello(path):
    observation = owm.weather_at_place(path)
    return str(observation.get_weather().get_temperature('celsius'))

if __name__ == "__main__":
    app.run()