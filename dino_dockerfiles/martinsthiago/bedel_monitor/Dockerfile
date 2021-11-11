FROM node:6.9.1
MAINTAINER 'Martins <rogue.thiago@gmail.com>'

ADD scripts       /monitor/scripts
ADD monitor.js    /monitor
ADD entrypoint.sh /monitor
ADD package.json  /monitor

WORKDIR /monitor

RUN npm install

CMD ["./entrypoint.sh"]