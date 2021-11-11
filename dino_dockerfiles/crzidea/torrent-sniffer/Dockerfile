FROM node:8-slim

COPY package.json package-lock.json /application/
WORKDIR /application
ENV NO_COLOR=1
RUN apt-get update && \
    apt-get install -y python make g++ && \
    npm install --production && \
    npm cache clean --force && \
    apt-get purge -y python make g++ && \
    apt-get autoremove -y && \
    apt-get clean

COPY . /application

VOLUME /root/.torrent-sniffer
EXPOSE 20000/udp

CMD npm start
