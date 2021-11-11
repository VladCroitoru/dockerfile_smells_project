FROM nginx:1.13-alpine
LABEL maintainer="Leif Gensert <leif@leif.io>"

# install necessary dependencies
RUN apk add --no-cache --virtual .run-deps \
    bash ca-certificates openssl \
    && update-ca-certificates

# reset default config
RUN rm /etc/nginx/conf.d/*

COPY nginx.conf /etc/nginx/nginx.conf

RUN mkdir -p /etc/nginx/sites-enabled/
RUN mkdir -p /etc/nginx/templates/
COPY *.template /etc/nginx/templates/
COPY entrypoint.sh /usr/local/bin

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

# SSL

RUN mkdir -p /var/www/letsencrypt
RUN mkdir -p /etc/letsencrypt

CMD ["nginx", "-g", "daemon off;"]
