FROM node:8.1.2-alpine
MAINTAINER Niek Palm <dev.npalm@gmail.com>

WORKDIR /app

ADD src /app/src
ADD package.json /app/

RUN yarn install && yarn run build && yarn install --production=true
RUN rm -rf src && rm -rf package.json

EXPOSE 4000

CMD ["node","/app/dist/server.js"]
