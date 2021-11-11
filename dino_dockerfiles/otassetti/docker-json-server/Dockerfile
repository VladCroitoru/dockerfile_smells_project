FROM node:latest
MAINTAINER Christian Lück <christian@lueck.tv>

RUN npm install -g json-server

WORKDIR /data
VOLUME /data

ADD run.sh /run.sh
ENTRYPOINT ["bash", "/run.sh"]
CMD []
