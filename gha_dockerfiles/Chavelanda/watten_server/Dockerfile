FROM python:3.6

WORKDIR usr/src/flask_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

COPY ./init_db.sh /init_db.sh

RUN chmod +x /init_db.sh

EXPOSE 5000

COPY . .

ENV  APP_SETTINGS="config.ProductionConfig"

CMD gunicorn --bind 0.0.0.0:$PORT wsgi:server
