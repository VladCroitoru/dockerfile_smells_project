# VERSION 1.1.0
FROM radektomasek/keboola-base-node
MAINTAINER Radek Tomasek <radek.tomasek@gmail.com>

WORKDIR /home

RUN git clone https://github.com/radektomasek/keboola-ex-sailthru ./ && git checkout tags/1.1.0 && npm install

ENTRYPOINT node_modules/.bin/babel-node --presets es2015,stage-0 ./src/index.js --data=/data
