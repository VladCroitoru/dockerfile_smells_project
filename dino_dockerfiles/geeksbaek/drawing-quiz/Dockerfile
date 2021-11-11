FROM ubuntu

RUN apt-get update && apt-get -y install nodejs npm

COPY /app /app

WORKDIR /app
RUN npm install

CMD nodejs server.js

EXPOSE 80