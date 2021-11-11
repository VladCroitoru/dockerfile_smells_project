FROM node:latest
MAINTAINER Firef0x

ENV PORT 3003
ENV REFRESHED_AT 20160308233000
ENV WEBROOT /var/www
ENV SRV_WEBROOT ${WEBROOT}/json-server

RUN npm install -g nrm \
 && nrm use taobao \
 && npm install -g forever \
 && mkdir -p ${SRV_WEBROOT} \
 && mkdir -p ${SRV_WEBROOT}/db \
 && mkdir -p ${SRV_WEBROOT}/log

ADD client/ ${SRV_WEBROOT}/client/
ADD lib/ ${SRV_WEBROOT}/lib/
ADD index.js ${SRV_WEBROOT}/index.js
ADD package.json ${SRV_WEBROOT}/package.json
ADD run ${SRV_WEBROOT}/run
ADD server.js ${SRV_WEBROOT}/server.js
ADD webpack.config.babel.js ${SRV_WEBROOT}/webpack.config.babel.js

RUN cd ${SRV_WEBROOT}/ \
 && npm install \
 && chmod 755 ${SRV_WEBROOT}/run

EXPOSE ${PORT}/tcp

VOLUME ["${SRV_WEBROOT}/db", "${SRV_WEBROOT}/log"]

WORKDIR "${SRV_WEBROOT}"
CMD ["${SRV_WEBROOT}/run"]
