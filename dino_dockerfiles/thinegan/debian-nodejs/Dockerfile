FROM debian:jessie
MAINTAINER Thinegan Ratnam <thinegan@thinegan.com>

RUN apt-get update && apt-get install -y curl sudo
RUN curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -
RUN apt-get update && apt-get install -y supervisor nodejs build-essential
RUN curl https://www.npmjs.com/install.sh | sh
RUN mkdir -p /var/nodejs/

ADD supervisord.conf /etc/supervisor/supervisord.conf
ADD supervisor-config/node.sv.conf /etc/supervisor/conf.d/

ADD package.json /var/nodejs/package.json
ADD app.js /var/nodejs/app.js

WORKDIR /var/nodejs
RUN npm install

EXPOSE 8080
# Define default command
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/supervisord.conf"]
