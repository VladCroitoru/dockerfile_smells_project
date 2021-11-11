FROM python:3.6-alpine3.7

EXPOSE 5555

WORKDIR /app
VOLUME ["/app"]
COPY . /app

RUN pip install .

ENV ARISEEM_CONFIG ./config.yml
ENV FLASK_APP ariseem/__main__.py
ENV FLASK_DEBUG 1
ENV FLASK_PORT 5555

CMD flask run --host=0.0.0.0 --port=$FLASK_PORT
