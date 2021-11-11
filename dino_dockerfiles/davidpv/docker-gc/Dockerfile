FROM gliderlabs/alpine:3.2

#ENV DOCKER_VERSION 1.7.1
ENV DOCKER_VERSION 1.13.0

RUN apk --update add bash curl tar \
  && curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz && tar --strip-components=1 -xvzf docker-${DOCKER_VERSION}.tgz -C /bin \
  && chmod +x /bin/docker \
  && apk del curl \
  && rm -rf /var/cache/apk/*

COPY ./docker-gc.sh /docker-gc.sh

VOLUME /var/lib/docker-gc.sh

CMD ["/docker-gc.sh"]
