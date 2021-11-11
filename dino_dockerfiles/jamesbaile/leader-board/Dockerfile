FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y nodejs
RUN apt-get install -y npm
RUN npm install -g http-server
RUN ln -s /usr/bin/nodejs /usr/bin/node

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY . /usr/src/app

EXPOSE 8080

CMD ["http-server", "-s"]