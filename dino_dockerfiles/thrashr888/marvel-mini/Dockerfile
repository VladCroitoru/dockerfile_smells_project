# DOCKER-VERSION 1.0.1

FROM peenuty/nodejs-npm-sass-docker

MAINTAINER Paul Thrasher "thrashr888@gmail.com"


WORKDIR /src

ADD package.json /src/
RUN npm install

ADD . /src

RUN bower install --allow-root

RUN npm install -g gulp

RUN cd /src; gulp build

EXPOSE  9000

CMD cd /src; gulp connect