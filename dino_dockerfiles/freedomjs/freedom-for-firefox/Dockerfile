# Dockerfile for a standard freedom-for-firefox instance

FROM selenium/node-firefox
MAINTAINER Will Scott <willscott@gmail.com>

USER root

RUN apt-get update -qqy \
  && apt-get -qqy install \
    nodejs nodejs-legacy git npm 

RUN npm install -g grunt-cli
ADD . /freedom-for-firefox
WORKDIR /freedom-for-firefox

RUN npm install

ENV DISPLAY :10

ENTRYPOINT ["/freedom-for-firefox/tools/docker-entrypoint.sh"]
