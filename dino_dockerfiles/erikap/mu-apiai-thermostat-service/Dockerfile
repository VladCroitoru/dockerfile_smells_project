FROM node:6

MAINTAINER Erika Pauwels <erika.pauwels@gmail.com>

ENV NODE_ENV production
ENV MU_SPARQL_ENDPOINT 'http://database:8890/sparql'
ENV MU_APPLICATION_GRAPH 'http://mu.semte.ch/application'

COPY mu-apiai-thermostat-service.sh /
COPY . /app/

RUN cd /app \
      && npm install -g nodemon \
      && npm install

EXPOSE 80
WORKDIR /app

CMD ["/bin/bash", "/mu-apiai-thermostat-service.sh"]