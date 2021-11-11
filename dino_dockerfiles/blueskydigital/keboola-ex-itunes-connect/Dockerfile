FROM radektomasek/keboola-base-node
MAINTAINER Radek Tomasek <radek.tomasek@gmail.com>

WORKDIR /home

# Initialize
RUN git clone https://github.com/blueskydigital/keboola-ex-itunes-connect ./ && npm install

ENTRYPOINT node_modules/.bin/babel-node --presets es2015,stage-0 ./src/index.js --data=/data
