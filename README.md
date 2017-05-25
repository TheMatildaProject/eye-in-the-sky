# Weather Api
A (really) simple weather forecast API written in Flask

## Installation

### Old School
```
pip install -r requirements.txt
python app.py <OWM_API_KEY>
```

### Docker
#### Build
`docker build --build-arg OWM_API_KEY=<OWM_API_KEY> . -t wapi`

#### One-off run
`docker run -d --name weather-api -p 5000:5000 wapi`

#### Run through docker compose
`docker-compose up -d`
