FROM ubuntu:14.04

RUN apt-get update
RUN apt-get install -y nodejs npm

ADD package.json /tmp/package.json
RUN cd /tmp && npm install
RUN mkdir -p /opt/app && cp -a /tmp/node_modules /opt/app/

WORKDIR /opt/app
ADD . /opt/app

EXPOSE 8080

# The following is only relevant on elastic beanstalk for the web service. fig will override it.
CMD ["nodejs", "index.js"]
