FROM alpine:3.4

RUN apk --no-cache add nodejs

ADD ./package.json /opt/explore-bot/package.json

WORKDIR /opt/explore-bot

RUN npm install

ADD . /opt/explore-bot

CMD npm start
