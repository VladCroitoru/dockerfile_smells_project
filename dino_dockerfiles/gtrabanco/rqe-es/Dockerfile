FROM node:7-alpine


RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD . /usr/src/app/
RUN npm install
RUN ./node_modules/.bin/gulp ts

EXPOSE 2180

CMD [ "npm", "start" ]