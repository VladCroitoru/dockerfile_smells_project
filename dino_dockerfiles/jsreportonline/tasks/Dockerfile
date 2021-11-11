FROM mhart/alpine-node
MAINTAINER Jan Blaha
EXPOSE 3000

RUN apk add --update curl

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app/
RUN npm install --production

COPY . /usr/src/app
COPY patch /usr/src/app

EXPOSE 3000

HEALTHCHECK CMD curl --fail http://localhost:3000 || exit 1

CMD [ "node", "index.js" ]