FROM node:16-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD . /usr/src/app

RUN apk add --update git

RUN npm install -g grunt && \
    npm install -g bower && \
    npm install && \
    bower install --allow-root

EXPOSE 8081

CMD ["run"]

ENTRYPOINT ["grunt"]
