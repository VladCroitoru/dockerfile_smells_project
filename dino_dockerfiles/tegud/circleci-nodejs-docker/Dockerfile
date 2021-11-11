FROM node:6.10.2

RUN set -x \
  && VER="17.03.0-ce" \
  && curl -L -o /tmp/docker-$VER.tgz https://get.docker.com/builds/Linux/x86_64/docker-$VER.tgz \
  && tar -xz -C /tmp -f /tmp/docker-$VER.tgz \
  && mv /tmp/docker/* /usr/bin \
  && mkdir /tmp/build \
  && npm i -g grunt-cli
