FROM alpine

RUN apk add --update \
    python \
    py-pip \
    && rm -rf /var/cache/apk/* \
    && pip install pipenv

WORKDIR /app
COPY . /app

RUN pipenv install --system --deploy

ENTRYPOINT ["/usr/bin/env", "python", "-m", "md_mqtt.server", "/config.yml"]
