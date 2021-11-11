FROM node:lts
MAINTAINER Aaditya Bhatia <aadityabhatia@gmail.com>

RUN npm i -g coffee-script

WORKDIR /data

COPY package.json /data/
RUN ["npm", "i"]

ENV NODE_ENV production
ENV PORT 8080
ENV CONTROLLER_PORT 8081

EXPOSE $PORT $CONTROLLER_PORT

COPY . /data/

RUN ["chown", "daemon:daemon", "public"]
USER daemon

CMD ["coffee", "app.coffee"]
