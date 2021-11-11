ARG REBUILD_INDEX=false

FROM python:3.7-alpine

RUN apk add --no-cache \
        g++ \
        git \
        libxslt-dev \
        mariadb-dev \
        jpeg-dev \
        zlib-dev \
        build-base

COPY requirements.txt /requirements.txt
RUN pip --no-cache-dir install -r /requirements.txt \
 && rm /requirements.txt

COPY . /app/.
WORKDIR /app
RUN rm -f .env \
 && rm -rf collected_static \
 && rm -rf media \
 && rm -rf downloads \
 && python manage.py collectstatic

CMD if [ "$REBUILD_INDEX" = "true" ] ; then \
 python manage.py search_index --rebuild -f && \
 gunicorn factotum.wsgi -c factotum/gunicorn.py \
; else \
 gunicorn factotum.wsgi -c factotum/gunicorn.py \
; fi

EXPOSE 8000 8001
VOLUME /app/collected_static
VOLUME /app/media
VOLUME /app/downloads
