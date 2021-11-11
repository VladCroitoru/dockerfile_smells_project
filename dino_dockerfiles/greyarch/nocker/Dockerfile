FROM node:7-alpine

ARG DOCKER_BUCKET=get.docker.com
ARG DOCKER_VERSION=17.03.0-ce

RUN apk add --no-cache curl \
 && curl -fSL "https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz" -o /tmp/docker.tgz \
 && tar -xzvf /tmp/docker.tgz -C /tmp/ \
 && mv /tmp/docker/docker /usr/local/bin/ \
 && rm -rf /tmp/* \
 && apk del curl

WORKDIR /work

CMD ["npm", "start"]
