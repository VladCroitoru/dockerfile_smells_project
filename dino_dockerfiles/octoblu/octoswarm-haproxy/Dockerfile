FROM haproxy:1.7-alpine
MAINTAINER Octoblu <docker@octoblu.com>
ENV DOCKER_VERSION 1.12.6

EXPOSE 80
EXPOSE 8080

RUN apk add --no-cache gettext bash jq curl

RUN curl -fsSLO "https://get.docker.com/builds/Linux/x86_64/docker-$DOCKER_VERSION.tgz" \
  && tar --strip-components=1 -xvzf "docker-$DOCKER_VERSION.tgz" -C /usr/local/bin \
  && chmod +x /usr/local/bin/docker \
  && rm "docker-$DOCKER_VERSION.tgz"

WORKDIR /usr/src/app
COPY run.sh haproxy.cfg.template backend.template /usr/src/app/
COPY static/ /usr/src/app/static/

CMD ["./run.sh"]
