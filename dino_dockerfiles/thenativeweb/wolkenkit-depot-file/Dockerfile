FROM thenativeweb/wolkenkit-box-node:2.0.0
MAINTAINER the native web <hello@thenativeweb.io>

ADD ./package.json /wolkenkit/

RUN cd /wolkenkit && \
    npm install --production --silent && \
    mkdir /blobs

ADD . /wolkenkit/
CMD [ "dumb-init", "node", "/wolkenkit/app.js" ]

ONBUILD ADD . /wolkenkit/app/
