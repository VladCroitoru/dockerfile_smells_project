FROM ubuntu:14.04
MAINTAINER Misa Ogura "misa.ogura01@gmail.com"

RUN apt-get -y update && apt-get install -y cowsay fortunes
ENV PATH $PATH:/usr/games/

CMD fortune -a | cowsay
