FROM ubuntu
MAINTAINER Michael Sauter <mail@michaelsauter.net>

ENV REFRESHED_AT 2014-02-19
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update

RUN DEBIAN_FRONTEND=noninteractive apt-get -y -q install ca-certificates
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q software-properties-common python-software-properties
RUN add-apt-repository -y ppa:chris-lea/node.js
RUN apt-get update

RUN DEBIAN_FRONTEND=noninteractive apt-get -y -q install wget
RUN DEBIAN_FRONTEND=noninteractive apt-get -y -q install nodejs

RUN wget https://github.com/hakimel/reveal.js/archive/2.6.1.tar.gz
RUN tar xzf 2.6.1.tar.gz
RUN mv /reveal.js-2.6.1 /revealjs

WORKDIR /revealjs

RUN npm install -g grunt-cli
RUN npm install
RUN sed -i Gruntfile.js -e 's/port: port,/port: port, hostname: "",/'

ADD index.html /revealjs/
ONBUILD ADD index.html /revealjs/
ONBUILD ADD css/ /revealjs/css/

EXPOSE 8000
CMD ["grunt", "serve"]