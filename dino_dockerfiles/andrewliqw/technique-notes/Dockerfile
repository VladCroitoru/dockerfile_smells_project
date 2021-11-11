FROM ubuntu:16.04

RUN apt-get -y update && apt-get -y upgrade && apt-get -y install python nodejs npm

RUN ln -s /usr/bin/nodejs /usr/local/bin/node && npm install npm@latest -g

COPY . /usr/src/technique-notes/

RUN cd /usr/src/technique-notes && PATH=/usr/local/bin:$PATH npm install

EXPOSE 8080

CMD /usr/local/bin/node /usr/src/technique-notes/server.js
