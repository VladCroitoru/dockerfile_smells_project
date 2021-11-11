FROM node:12.18.3
MAINTAINER Superbalist <tech+docker@superbalist.com>

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app/
RUN npm install --only=prod

COPY src /usr/src/app/src/

EXPOSE 3000
CMD ["node", "./src/bin/www"]
