FROM ubuntu
MAINTAINER Rowan Carr
 
RUN apt-get update && apt-get -yq install python-software-properties git build-essential curl
RUN curl -sL https://deb.nodesource.com/setup | sudo bash -
RUN apt-get -y install nodejs
 
RUN cd /tmp && npm install dynroute
RUN mkdir -p /opt/app && cp -a /tmp/node_modules /opt/app/

RUN ln -s /opt/app/node_modules/dynroute/bin/dynroute /bin/

CMD ["dynroute"]