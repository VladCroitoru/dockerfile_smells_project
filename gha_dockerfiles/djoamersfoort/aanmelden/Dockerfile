FROM python:3.8-alpine

# Set the file maintainer (your name - the file's author)
MAINTAINER Ronald Moesbergen

COPY requirements.txt /srv/aanmelden/requirements.txt

RUN apk update && \
    apk add nginx mariadb-dev zlib-dev gcc musl-dev sqlite && \
    pip3 install --no-cache-dir -r /srv/aanmelden/requirements.txt && \
    apk del gcc musl-dev

WORKDIR /srv
RUN mkdir static logs

COPY nginx.conf /etc/nginx/nginx.conf

# Port to expose
EXPOSE 80

COPY aanmelden/ /srv/aanmelden/
COPY manage.py  /srv

WORKDIR /srv
COPY start.sh /
COPY ./jobs.sh /
ENTRYPOINT ["/start.sh"]
