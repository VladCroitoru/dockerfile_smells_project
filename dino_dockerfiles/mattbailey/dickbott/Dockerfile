FROM node:11-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apk -U --no-cache add git python make
COPY package.json /usr/src/app/
COPY package-lock.json /usr/src/app/
RUN npm install --only=prod && npm cache clean --force
COPY . /usr/src/app

CMD [ "npm", "start" ]
