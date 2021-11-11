FROM alpine:3.6

RUN apk update \
 && apk upgrade \
 && apk add \
      bash \
      curl \
      dcron \
      git  \
 && rm -rf /var/cache/apk/*


# from https://github.com/spotify/docker-gc/blob/master/Dockerfile
ENV DOCKER_VERSION 17.09.0

RUN cd /tmp/ \
 && curl -sSL -O https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_VERSION}-ce.tgz \
 && tar zxf docker-${DOCKER_VERSION}-ce.tgz \
 && mkdir -p /usr/local/bin/ \
 && mv $(find . -type f -name 'docker') /usr/local/bin/ \
 && chmod +x /usr/local/bin/docker \
 && curl -sSL -O https://raw.githubusercontent.com/spotify/docker-gc/master/docker-gc \
 && mv docker-gc /usr/local/bin/ \
 && chmod +x /usr/local/bin/docker-gc \
 && apk del curl \
 && rm -rf /tmp/* 


COPY container-content/entry.sh /
COPY container-content/cronjob.config /

CMD ["/entry.sh"]

