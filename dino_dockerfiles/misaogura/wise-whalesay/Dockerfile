FROM docker/whalesay:latest
MAINTAINER Misa Ogura misa.ogura01@gmail.com

RUN apt-get -y update && apt-get install -y fortunes
ENV PATH $PATH:/usr/games/

CMD fortune -a | cowsay
