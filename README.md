# Eye in the sky
A (really) simple weather forecast API written in Flask

## Requirements
- Python or Docker
- Open Weather API Token, get one here: https://openweathermap.org/api

## Installation

### Old School
```
pip install -r requirements.txt
export FLASK_APP=app.py; export OWM_TOKEN=$OWM_API_KEY; flask run --host=0.0.0.0 --port=5000
```

### Docker
#### Build
`docker build --build-arg OWM_API_KEY=<OWM_API_KEY> . -t wapi`

#### One-off run
`docker run -d --name weather-api -p 5001:5000 wapi`

#### Run through docker compose
`docker-compose up -d`
 
## Usage
### Request Example
```
curl -H "Content-Type: application/json" -X POST -d '{"city":"New York"}' http://localhost:5000

```

### Response Example
```
{
  "forecast": "{'temp_max': 14.0, 'temp_kf': None, 'temp': 13.23, 'temp_min': 12.0}"
}
```
