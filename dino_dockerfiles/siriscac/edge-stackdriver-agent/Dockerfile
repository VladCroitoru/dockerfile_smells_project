FROM ubuntu:14.04

RUN apt-get update
RUN apt-get -qq -y install curl

RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
RUN apt-get install -y nodejs
RUN apt-get install -y rsyslog
RUN npm i -g pm2

COPY rsyslog.conf /etc/rsyslog.conf
COPY /agent /home/agent

WORKDIR /home/agent
RUN npm install

EXPOSE 514/udp
EXPOSE 601/tcp

CMD service rsyslog restart && pm2 start agent.js --no-daemon
