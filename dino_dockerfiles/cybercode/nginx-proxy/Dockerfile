FROM cybercode/alpine-nginx
MAINTAINER Rick Frankel rick (at) cybercode.nyc

ENV DOCKER_GEN_VERSION 0.7.3

# busybox wget doesn't support ssl, use curl...
RUN apk --update add curl && \
    curl -L https://github.com/jwilder/docker-gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-alpine-linux-amd64-$DOCKER_GEN_VERSION.tar.gz \
    |  tar -C /usr/local/bin -xvzf - \
    && chown root:root /usr/local/bin/docker-gen \
    && apk del curl && rm /var/cache/apk/*

WORKDIR /app/
ADD app /app

ENV DOCKER_HOST unix:///tmp/docker.sock

VOLUME ["/etc/nginx/certs"]

ENTRYPOINT ["/app/docker-entrypoint.sh"]
CMD ["nginx"]
