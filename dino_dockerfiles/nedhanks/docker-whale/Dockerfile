FROM docker/whalesay:latest
MAINTAINER Ned Hanks <ned.hanks@octanner.com>

RUN apt-get -y update && apt-get install -y fortunes

CMD /usr/games/fortune -a | cowsay -f squirrel
