FROM node:14.0-alpine

ENV NODE_ENV production
ENV FORCE_COLOR 1

RUN apk add --update git

RUN mkdir -p /ck && mkdir -p /app
WORKDIR /app

COPY package.json /ck/
RUN cd /ck && npm install --production
COPY . /ck

RUN chmod 777 /ck/index.js && ln -s /ck/index.js /usr/local/bin/clientkit

ENTRYPOINT ["/usr/local/bin/clientkit"]
