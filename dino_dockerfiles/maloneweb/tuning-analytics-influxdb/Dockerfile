FROM mhart/alpine-node:8
MAINTAINER Malone Tuning <web@malonetuning.com>
LABEL maintainer="Malone Tuning <web@malonetuning.com>"

WORKDIR /app
COPY ./src /app/src
COPY package.json /app
COPY package-lock.json /app

RUN npm install

CMD ["npm", "run", "dev"]
