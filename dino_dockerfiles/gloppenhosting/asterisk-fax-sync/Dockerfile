FROM mhart/alpine-node:5.4.1
MAINTAINER Andreas Krüger
ENV NODE_ENV production
ENV NODE_DEBUG false

RUN apk update
RUN apk add ghostscript tiff-dev

COPY /server.js /server.js
COPY /package.json /package.json
COPY /faxprocessor.js /faxprocessor.js
COPY /config /config

RUN npm install

CMD ["node", "--es_staging", "server.js"]
