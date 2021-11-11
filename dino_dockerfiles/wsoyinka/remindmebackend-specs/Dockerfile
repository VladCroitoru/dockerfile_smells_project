FROM ubuntu:xenial

MAINTAINER wale soyinka <wsoyinka@gmail.com>

ENV TERM=xterm-256color

RUN sed -i "s/http:\/\/archive./http:\/\/ca.archive./g" /etc/apt/sources.list

RUN 	apt-get update &&\
    	apt-get install curl -y && \
 	curl -sL https://deb.nodesource.com/setup_4.x | bash - && \
	apt-get -y install nodejs

COPY . /app
WORKDIR /app


RUN 	npm install -g mocha && \
	npm install


ENTRYPOINT ["mocha"]
 
