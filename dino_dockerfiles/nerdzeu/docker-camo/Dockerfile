FROM node:14.0.0
MAINTAINER Paolo Galeone <nessuno@nerdz.eu>

RUN git clone --recursive https://github.com/atmos/camo /opt/camo
WORKDIR /opt/camo/

RUN npm install

USER nobody
ENTRYPOINT npm start

EXPOSE 8081
