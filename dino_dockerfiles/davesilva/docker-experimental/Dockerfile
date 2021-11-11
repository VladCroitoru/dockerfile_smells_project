FROM docker:18.03.1-ce

RUN mkdir /root/.docker
ADD client-config.json /root/.docker/config.json

RUN apk add --no-cache git bash jq parallel
