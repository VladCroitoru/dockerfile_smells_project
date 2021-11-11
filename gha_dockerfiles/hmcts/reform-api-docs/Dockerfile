FROM node:8.1.4

MAINTAINER "HMCTS Reform"
LABEL maintainer="HMCTS Reform"

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json .
COPY package-lock.json .
RUN npm install

COPY . .

EXPOSE 4000
CMD [ "npm", "start" ]
