FROM node:lts

COPY package*.json ./
COPY *.js ./

RUN apt-get update
RUN apt-get install apt-transport-https
RUN wget -qO- https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN wget -qO- https://storage.googleapis.com/download.dartlang.org/linux/debian/dart_stable.list > /etc/apt/sources.list.d/dart_stable.list
RUN apt-get update
RUN apt-get install dart

EXPOSE 3000
EXPOSE 22000

RUN npm install

CMD [ "node", "start.js", "--debug" ]
