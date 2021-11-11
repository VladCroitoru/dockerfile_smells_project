FROM node:5.5-wheezy

RUN apt-get update

RUN apt-get install graphicsmagick -y

RUN mkdir -p /usr/src/cumulus-cloud

COPY package.json /usr/src/cumulus-cloud/package.json
WORKDIR /usr/src/cumulus-cloud
RUN npm install

EXPOSE 10088
EXPOSE 80

COPY . /usr/src/cumulus-cloud

ENV REDIS_DB DB
ENV REDIS_PORT 6379
ENV URL_HOST 192.168.99.100
ENV URL_SSL_SECURITY auto
ENV URL_PORT 10088
ENV URL_PATHNAME /file

VOLUME /usr/src/cumulus-cloud/store


CMD ["node", "bootstrap/register.js"]
