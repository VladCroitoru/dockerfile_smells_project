FROM mhart/alpine-node:latest

ARG APK_REPO_FILE=shared_files/apk/alpine_default
ADD $APK_REPO_FILE /etc/apk/repositories

RUN apk update && \
    apk add ca-certificates && \
    update-ca-certificates && \
    apk add nginx

# Setup NGINX
COPY shared_files/nginx/nginx.conf /etc/nginx/nginx.conf
RUN mkdir -p /etc/nginx/conf.d
RUN mkdir -p /run/nginx/

# Use confd for templating from environment variables
# See https://github.com/kelseyhightower/confd
RUN apk add confd@edge_testing && \
    mkdir -p /etc/confd/{conf.d,templates}
COPY shared_files/confd/*.toml /etc/confd/conf.d/
COPY shared_files/confd/*.tmpl /etc/confd/templates/

# Setup Certbot for https site (enable .well-known verification)
RUN apk add certbot
COPY shared_files/nginx/default.conf /etc/nginx/conf.d/default.conf

# NGINX https site will be setup and at runtime with
# the SECURE_DOMAIN_NAME environment variable via the `secure_start` script
COPY shared_files/secure_start /usr/local/bin/secure_start
RUN chmod 550 /usr/local/bin/secure_start

### TODO: Add cron job to renew the cert twice a day

VOLUME /etc/nginx/conf.d
VOLUME /etc/letsencrypt
VOLUME /etc/confd
VOLUME /usr/src

EXPOSE 80 443
