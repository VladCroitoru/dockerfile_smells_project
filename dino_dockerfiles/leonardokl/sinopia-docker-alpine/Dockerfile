FROM mhart/alpine-node:6
MAINTAINER Leonardo Luiz <leonardokl@hotmail.com>

RUN mkdir -p /opt/sinopia/storage

WORKDIR /opt/sinopia
RUN npm install js-yaml sinopia
COPY /config.yaml /opt/sinopia/
CMD ["node", "./node_modules/sinopia/bin/sinopia", "--config", "./config.yaml"]

EXPOSE 4873
