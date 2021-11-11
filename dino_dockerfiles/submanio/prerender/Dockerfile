FROM ubuntu:14.04
MAINTAINER Vladimir Iakovlev <nvbn.rm@gmail.com>

RUN apt-get update -yqq
RUN apt-get upgrade -yqq
RUN apt-get install software-properties-common python-software-properties -yqq --no-install-recommends
RUN add-apt-repository ppa:chris-lea/node.js  -y
RUN apt-get update -yqq
RUN apt-get install nodejs git build-essential libfreetype6 libfontconfig -yqq --no-install-recommends

RUN git clone https://github.com/prerender/prerender.git
WORKDIR prerender
RUN npm install
COPY server.js .

CMD node server.js
