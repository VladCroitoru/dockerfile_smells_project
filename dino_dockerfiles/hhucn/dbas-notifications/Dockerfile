FROM alpine
MAINTAINER Christian Meter <meter@cs.uni-duesseldorf.de>, Tobias Krauthoff <krauthoff@cs.uni-duesseldorf.de>

RUN apk add --no-cache nodejs yarn

RUN mkdir -p /code/log
WORKDIR /code

ADD . /code

RUN yarn install

EXPOSE 5222
CMD ["node", "server.js", "-g", "-lc", "-lf", "-p", "/cert/live/dbas.cs.uni-duesseldorf.de/"]
