FROM node:14-alpine
WORKDIR /usr/src/app

RUN apk add --no-cache git
RUN npm install -global pm2
RUN npm install -global lerna

COPY . .
RUN npm run install:prod

RUN npm uninstall -global lerna
RUN apk del git

EXPOSE 8081-8095

CMD [ "pm2-runtime", "pm2.json" ]

