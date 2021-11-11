FROM alpine
MAINTAINER ZiaxDK

WORKDIR /usr/src/app
COPY . /usr/src/app/

RUN apk add --update nodejs-lts && \
    mkdir -p /usr/src/app/uploads && \
    npm install

CMD [ "npm", "start" ]
