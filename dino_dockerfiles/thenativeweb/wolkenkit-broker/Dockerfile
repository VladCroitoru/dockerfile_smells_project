FROM thenativeweb/wolkenkit-box-node:3.1.0
MAINTAINER the native web <hello@thenativeweb.io>

ADD ./package.json /wolkenkit/

RUN cd /wolkenkit && \
    npm install --production --silent

ADD . /wolkenkit/
RUN rm -rf /wolkenkit/app
# CMD is set programmatically by the wolkenkit CLI.

ONBUILD ADD . /wolkenkit/app/
