FROM python:3.6-alpine
MAINTAINER Mopsalarm

COPY requirements.txt /tmp/

RUN apk update \
 && apk add ca-certificates postgresql-libs postgresql-dev python3-dev gcc musl-dev \
 && pip install -r /tmp/requirements.txt \
 && apk del postgresql-dev python3-dev gcc musl-dev \
 && rm -rf /var/cache/apk

COPY . /app/

EXPOSE 8080

ENV PYTHONPATH=/app PYTHONUNBUFFERED=1

ENTRYPOINT ["/usr/local/bin/python3", "-m", "bottle", "-s", "cherrypy", "-b", "0.0.0.0:8080", "--debug", "main"]
