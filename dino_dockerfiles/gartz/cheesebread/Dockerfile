FROM node:6.9.4
MAINTAINER Gabriel Reitz Giannattasio <g@gartz.me>

ENV PORT=3000 HOST=0.0.0.0 CACHE_DIR=/cache LOG=true EXTERNAL_URL=http://localhost:3000

EXPOSE 3000

WORKDIR /cheese-bread-js

COPY package.json server.js lib.js cli.js ./

VOLUME /cache

RUN npm install \
    && rm -Rf ~/.npm

CMD npm start
