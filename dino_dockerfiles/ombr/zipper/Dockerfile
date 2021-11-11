FROM node:alpine
MAINTAINER Luc Boissaye <luc@boissaye.fr>

COPY . /var/app
WORKDIR /var/app
RUN npm install

EXPOSE 5000
CMD npm run start
