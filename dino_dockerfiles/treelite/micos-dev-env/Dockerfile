FROM node:6
MAINTAINER treelite <c.xinle@gmail.com>

RUN apt-get update
RUN apt-get install nasm
RUN mkdir /micos

WORKDIR /micos

VOLUME ["/micos"]

ENTRYPOINT ["make"]
