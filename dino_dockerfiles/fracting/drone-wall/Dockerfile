# see https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/ for Dockerfile best practices

# build me with:
# docker build -t "juicymo/drone-wall:1.0.0" .

FROM node
MAINTAINER Tomas Jukin <tomas.jukin@juicymo.cz>

RUN \
  apt-get update &&\
  apt-get install -y git curl wget

RUN git clone -b master https://github.com/taueres/drone-wall.git /app
WORKDIR /app
RUN \
  npm install &&\
  npm install -g bower &&\
  npm install -g grunt-cli &&\
  bower --allow-root install &&\
  grunt
#  grunt deploy

EXPOSE 3000
CMD API_SCHEME=$API_SCHEME API_DOMAIN=$API_DOMAIN API_TOKEN=$API_TOKEN node server.js