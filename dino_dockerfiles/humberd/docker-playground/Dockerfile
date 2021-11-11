# docker-machine env default | Invoke-Expression
FROM node:8.3.0-alpine
MAINTAINER Humberd

ADD package.json /tmp
ADD package-lock.json /tmp
RUN cd /tmp && npm install
RUN mkdir -p /usr/src/app && cp -a /tmp/node_modules /usr/src/app/

WORKDIR /usr/src/app

COPY . .

EXPOSE 4321

CMD ["npm", "start"]
