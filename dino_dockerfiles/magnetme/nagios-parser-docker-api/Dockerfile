FROM node:8.9
MAINTAINER Rogier Slag <Rogier@magnet.me>

RUN mkdir /opt/src
VOLUME ["/opt/nagios"]
EXPOSE 8080

WORKDIR /opt/src
ADD package.json /opt/src
ADD yarn.lock /opt/src
RUN yarn install
ADD src/ /opt/src

CMD ["node", "/opt/src/index.js", "--allow-all-cors", "--with-ws"]

