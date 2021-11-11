FROM node:12.18.3-alpine as builder
RUN apk update
RUN apk add --update bash
RUN npm install -g npm@7.23.0

RUN apk add git
RUN npm install -g --unsafe-perm polymer-cli
RUN npm install -g typescript


WORKDIR /tmp
ADD package.json /tmp/
ADD package-lock.json /tmp/

RUN npm install --no-save

ADD . /code/
WORKDIR /code
RUN cp -a /tmp/node_modules /code/node_modules
RUN npm run build


FROM node:12.18.3-alpine
RUN apk update
RUN apk add --update bash

WORKDIR /code
RUN npm install express --no-save
RUN npm install browser-capabilities@1.1.3 --no-save
COPY --from=builder /code/express.js /code/express.js
COPY --from=builder /code/build /code/build
EXPOSE 8080
CMD ["node", "express.js"]