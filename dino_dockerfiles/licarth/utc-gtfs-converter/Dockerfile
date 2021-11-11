FROM node:6

WORKDIR /opt/src

RUN wget -qO /usr/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.1.0/dumb-init_1.1.0_amd64 && chmod +x /usr/bin/dumb-init
ADD package.json /opt/src/package.json
RUN npm install
ADD . /opt/src
RUN npm install -g

ENTRYPOINT ["utc-gtfs-converter"]
