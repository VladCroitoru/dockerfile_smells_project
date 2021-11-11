FROM node:boron-alpine

WORKDIR /usr/src/app
COPY package.json package-lock.json /usr/src/app/

RUN apk update && \
    apk upgrade && \
    npm install --production && \
    chmod 1777 /tmp

COPY . /usr/src/app

USER node:node
EXPOSE 3006
ENV NODE_ENV=production

CMD [ "node", "server.js" ]
