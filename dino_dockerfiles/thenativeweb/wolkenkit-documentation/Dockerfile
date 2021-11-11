FROM thenativeweb/wolkenkit-box-node:3.1.0
MAINTAINER the native web <hello@thenativeweb.io>

ADD . /documentation/

WORKDIR /documentation

RUN npm install --production --silent

CMD [ "dumb-init", "node", "app.js" ]
