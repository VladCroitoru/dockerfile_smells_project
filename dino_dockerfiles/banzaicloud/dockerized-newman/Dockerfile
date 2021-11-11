FROM postman/newman_alpine33:3.8.2

RUN apk add --no-cache openssl

ENV DOCKERIZE_VERSION v0.5.0
RUN wget \
    https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

ENV PIPELINE_ENDPOINT http://0.0.0.0:9090
ENV POSTMAN_COLLECTION https://www.getpostman.com/collections/7a4c9291ff7b1afe5a5e

ADD newman/env.tmpl /etc/newman/env.tmpl

ENTRYPOINT dockerize \-template /etc/newman/env.tmpl:/etc/newman/env.json \
   newman run "$POSTMAN_COLLECTION" --environment="/etc/newman/env.json"
