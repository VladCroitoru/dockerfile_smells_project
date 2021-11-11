FROM python:3.6-alpine

WORKDIR /app

RUN apk add --update --no-cache \
    nodejs \
    postgresql-dev \
    libpq \
    libffi \
    libffi-dev \
    libxml2-dev \
    libxslt-dev \
    python3-dev \
    libstdc++ \
    redis \
    && apk --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ --update add \
    leveldb \
    leveldb-dev

ADD requirements.txt .

RUN apk add --update --no-cache --virtual .build-deps \
    build-base \
    ca-certificates \
    g++ \
    nodejs-npm \
    && update-ca-certificates \
    && pip3 install -r requirements.txt \
    && npm install -g os-types@1.17 \
    && apk del --no-cache .build-deps

# ADD repos/datapackage-pipelines-fiscal ./datapackage-pipelines-fiscal
# RUN pip install -e ./datapackage-pipelines-fiscal

ADD initialize.sh initialize.sh

ENV PATH "$PATH:/app/node_modules/.bin"

EXPOSE 5000

CMD /app/initialize.sh
