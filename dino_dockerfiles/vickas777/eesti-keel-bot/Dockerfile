FROM node:carbon-alpine

RUN apk update && apk upgrade
RUN apk add --update bash
RUN rm -rf /var/cache/apk/*

WORKDIR /app
COPY index.js /app/index.js
COPY package.json /app/package.json

#RUN npm install gulp bower -g

RUN cd /app && npm i --only=prod

# Starting server
CMD ["node", "/app/index.js"]
