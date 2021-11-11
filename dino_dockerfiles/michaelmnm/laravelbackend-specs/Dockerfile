FROM ubuntu:trusty
MAINTAINER Michael Mandato <mmandato@helloencom.co>

ENV TERM=term-256color

RUN apt-get update && \
	apt-get install curl -y && \
	curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - && \
	apt-get install -y nodejs

COPY . /app
WORKDIR /app

RUN npm install -g mocha && \
	npm install

ENTRYPOINT ["mocha"]