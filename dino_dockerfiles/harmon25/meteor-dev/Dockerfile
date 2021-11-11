FROM debian:latest

MAINTAINER harmoN25 "nomraharmon@gmail.com"

ENV METEOR_DIR /opt/meteor-dev

COPY scripts $METEOR_DIR

RUN bash $METEOR_DIR/init.sh
RUN mkdir /opt/app
WORKDIR /opt/app

EXPOSE 3000

ENTRYPOINT bash $METEOR_DIR/startup.sh