FROM node:alpine

RUN apk update
RUN apk add git

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app

RUN npm install --unsafe-perm

EXPOSE 8080

CMD [ "npm", "start" ]
