# Name: sergeyd/SD.SQS

# DOCKER-VERSION 0.10.0

FROM ubuntu:15.10

# Install Node.js and npm
RUN 	apt-get update
RUN     apt-get -y install nodejs
RUN     apt-get -y install npm

# Bundle app source
COPY . /
# Install app dependencies

EXPOSE 9000

RUN  npm install

ENTRYPOINT ["nodejs", "worker.js"]
