FROM raxetul/alpine-s6-base

LABEL maintainer="Emrah URHAN <raxetul@gmail.com>"

COPY nginx-service /s6/nginx-service
RUN apk update && apk add --no-cache \
        nginx \
      && rm -rf /var/cache/apk/* \
      && chmod +x /s6/nginx-service/run /s6/nginx-service/finish \
      && chown root /s6/nginx-service/run /s6/nginx-service/finish \
      && mkdir -p /run/nginx && touch /run/nginx/nginx.pid \
      && rm -rf /var/cache/apk/*
## Don't setup ENTRYPOINT, it is set to s6 superviser in alpine-s6-base image, see Dockerfile of alpine-s6-base image
