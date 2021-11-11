FROM alpine:latest
MAINTAINER playniuniu@gmail.com

WORKDIR /usr/src/app/
COPY . /usr/src/app/

RUN apk add --update --no-cache nodejs nginx \
    && npm install \
    && npm run build \
    && apk del nodejs \
    && rm -rf /var/cache/apk/* \
    && rm -rf ./node_modules/ \
    && rm -f /etc/nginx/nginx.conf \
    && cp ./nginx.conf /etc/nginx/

EXPOSE 80

ENTRYPOINT ["nginx"]
