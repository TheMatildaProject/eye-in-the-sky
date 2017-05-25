FROM python:3.6.1-alpine
MAINTAINER Edward Leoni

ARG OWM_API_KEY

RUN mkdir /app
WORKDIR /app

ADD . .

RUN echo "export FLASK_APP=/app/app.py; export OWM_TOKEN=$OWM_API_KEY; flask run --host=0.0.0.0 --port=5000" > run.sh

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["sh", "run.sh"]
