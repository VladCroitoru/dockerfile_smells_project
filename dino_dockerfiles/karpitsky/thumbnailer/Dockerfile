FROM python:3.6-alpine3.7

RUN apk --no-cache add \
        gcc \
        musl-dev \
        libjpeg-turbo-dev \
        zlib-dev \
        ca-certificates \
        ffmpeg \
        libmagic \
    && rm -rf /var/cache/*


WORKDIR /usr/src/app

ADD requirements.txt /usr/src/app
RUN pip install -U --src /usr/local/src --no-cache-dir -r requirements.txt

COPY . /usr/src/app
ENV PYTHONUNBUFFERED 1