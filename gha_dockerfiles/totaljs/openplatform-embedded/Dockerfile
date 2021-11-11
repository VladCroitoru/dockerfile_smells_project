FROM node:16
MAINTAINER totaljs "info@totaljs.com"

VOLUME /www
WORKDIR /www
RUN mkdir -p /www/bundles

COPY config .
COPY index.js .
COPY guest.json .
COPY package.json .
COPY openplatform.bundle ./bundles/

RUN npm install
EXPOSE 8000

CMD [ "npm", "start" ]