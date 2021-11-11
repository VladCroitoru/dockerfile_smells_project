FROM radektomasek/keboola-base-node
MAINTAINER Radek Tomasek <radek.tomasek@gmail.com>

WORKDIR /home

# Initialize
RUN git clone https://github.com/radektomasek/keboola-ex-dropbox-v1 ./ && npm install

ENTRYPOINT node ./src/index.js --data=/data
