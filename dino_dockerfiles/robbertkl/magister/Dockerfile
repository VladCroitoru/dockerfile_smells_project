FROM node:alpine
MAINTAINER Robbert Klarenbeek <robbertkl@renbeek.nl>

WORKDIR /app

COPY package*.json ./
RUN npm ci
COPY . .

ENTRYPOINT [ "node", "app" ]
CMD []
