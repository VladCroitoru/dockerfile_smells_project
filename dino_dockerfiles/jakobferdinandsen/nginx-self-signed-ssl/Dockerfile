FROM debian:latest

RUN apt-get clean && apt-get update && apt-get install -my \
    openssl

RUN mkdir -p /ssl

RUN openssl req -new -newkey rsa:4096 -days 365 -nodes -x509 \
    -subj "/C=DK/ST=Sjaelland/L=City/O=Org/CN=WompWomp" \
    -keyout /ssl/ssl.key -out /ssl/ssl.crt

FROM nginx:stable

COPY --from=0 /ssl/ssl.key /usr/local/etc/nginx/ssl/ssl.key
COPY --from=0 /ssl/ssl.crt /usr/local/etc/nginx/ssl/ssl.crt

COPY ssl.conf /etc/nginx/conf.d/default.conf
