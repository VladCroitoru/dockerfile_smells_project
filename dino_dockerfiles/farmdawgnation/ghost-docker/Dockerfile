FROM node:10.15.0-slim

MAINTAINER Matt Farmer <matt@frmr.me>

RUN apt-get update && \
  apt-get install -y zip unzip dumb-init python build-essential && \
  apt-get clean

ENV GHOSTVER 2.22.3

ADD https://github.com/TryGhost/Ghost/releases/download/$GHOSTVER/Ghost-$GHOSTVER.zip /opt

RUN unzip /opt/Ghost-$GHOSTVER.zip -d /opt/ghost

WORKDIR /opt/ghost

ENV DEBIAN_FRONTEND noninteractive

RUN adduser ghost

RUN chown -R ghost:ghost /opt/ghost

ADD docker-command.sh /opt/docker-command.sh

RUN chown ghost:ghost /opt/docker-command.sh && \
  chmod 755 /opt/docker-command.sh

USER ghost

RUN npm install

ENTRYPOINT ["dumb-init", "--"]

CMD ["/opt/docker-command.sh"]

EXPOSE 2368
