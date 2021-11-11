FROM tozd/runit

EXPOSE 5000/tcp

RUN apt-get update -q -q && \
 apt-get install --yes --force-yes nodejs nodejs-legacy npm adduser git && \
 adduser --system --group exposer --home /home/exposer

COPY . /exposer

RUN export NODE_ENV=production && \
 cd /exposer && \
 npm install && \
 ./node_modules/.bin/browserify client.js -p ./configure -o static/bundle.js

COPY ./etc /etc
