
FROM ubuntu:14.04

WORKDIR /usr/app

RUN apt-get update -y -q && apt-get upgrade -y -q

RUN apt-get update
RUN apt-get install gcc make
RUN apt-get install golang-1.10

COPY .env /usr/app/.env

CMD [ "ls" ]
