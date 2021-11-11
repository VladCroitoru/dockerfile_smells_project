FROM mhart/alpine-node:7
MAINTAINER denso.ffff@gmail.com

#RUN apk add --no-cache make gcc g++ python
RUN npm install -g gulp yarn@0.18


COPY package.json /srv/package.json
RUN cd /srv/ && yarn && rm -fr ~/.cache
RUN npm install -g nodemon

WORKDIR /srv/www
COPY . /srv/www/

EXPOSE 5002
CMD cd /srv/www/ && nodemon server.js
