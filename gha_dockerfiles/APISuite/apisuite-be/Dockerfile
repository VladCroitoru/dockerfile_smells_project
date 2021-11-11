FROM node:14-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package*.json /usr/src/app/
COPY . /usr/src/app/

RUN apk update \
    && apk --no-cache add --virtual build-dependencies build-base python \
    && npm install --only=prod \
    && npm rebuild bcrypt --build-from-source \
    && apk del build-dependencies

EXPOSE 6001

CMD ["node", "app.js"]

