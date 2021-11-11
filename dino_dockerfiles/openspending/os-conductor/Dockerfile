FROM python:3.6-alpine

WORKDIR /app

RUN apk add --update --no-cache \
    libpq \
    postgresql-dev \
    libffi \
    libffi-dev \
    bash \
    curl \
    libstdc++ \
    nodejs \
    && apk --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ --update add \
    leveldb \
    leveldb-dev

COPY requirements.txt .

RUN apk add --update --no-cache --virtual=build-dependencies \
    build-base \
    git \
    nodejs-npm \
    && pip install -r requirements.txt \
    && npm install -g os-types@1.15.1 \
    && apk del build-dependencies \
    && rm -rf /var/cache/apk/*

COPY config.yml config.yml
COPY docker/startup.sh /startup.sh
COPY docker/docker-entrypoint.sh /entrypoint.sh
COPY conductor conductor

EXPOSE 8000

CMD ["/startup.sh"]
ENTRYPOINT ["/entrypoint.sh"]
