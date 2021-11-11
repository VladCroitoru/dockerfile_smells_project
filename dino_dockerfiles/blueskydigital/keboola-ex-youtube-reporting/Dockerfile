FROM radektomasek/keboola-base-node
MAINTAINER Radek Tomasek <radek.tomasek@gmail.com>

WORKDIR /home

RUN rpm --rebuilddb && yum update -y nss curl libcurl && git clone https://github.com/blueskydigital/keboola-ex-youtube-reporting ./ && npm install

ENTRYPOINT node_modules/.bin/babel-node --presets es2015,stage-0 ./src/index.js --data=/data
