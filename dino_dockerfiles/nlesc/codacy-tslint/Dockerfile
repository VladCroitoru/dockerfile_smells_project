FROM mhart/alpine-node:6

MAINTAINER Stefan Verhoeven <s.verhoeven@esciencecenter.nl>

RUN adduser -u 2004 -D docker

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN npm install -g 

WORKDIR /src

USER docker

VOLUME /src

CMD ["/usr/bin/codacy-tslint"]
