FROM ubuntu:xenial
MAINTAINER Jan Blaha
EXPOSE 5488

RUN apt-get update && apt-get install -y curl sudo && \
    curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - && \
    apt-get install -y nodejs docker.io

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app/
RUN npm install --production

COPY . /usr/src/app

EXPOSE 1000

HEALTHCHECK CMD curl --fail http://localhost:1000 || exit 1

CMD [ "node", "index.js" ]