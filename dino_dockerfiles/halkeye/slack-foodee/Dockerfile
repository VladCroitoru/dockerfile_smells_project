FROM node:8.4
MAINTAINER Gavin Mogan <docker@gavinmogan.com>
EXPOSE 3000

WORKDIR /usr/src/app
COPY . /usr/src/app/
RUN rm -rf package-lock.json
RUN NODE_ENV=development npm install
RUN npm test
RUN rm -rf node_modules package-lock.json
RUN NODE_ENV=production npm install
CMD npm run start

