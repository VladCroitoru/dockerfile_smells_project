FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /code

RUN mkdir -p /var/www/music_player/static && mkdir -p /var/www/music_player/media \
    && apk update && apk add build-base postgresql-dev gcc zlib-dev jpeg-dev

COPY . /code/
COPY ./media/ /var/www/music_player/media/

RUN chmod +x /code/entrypoint.sh && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && addgroup -S app && adduser -S app -G app \
    && chown -R app:app /code \ 
    && chown -R app:app /var/www/music_player/

