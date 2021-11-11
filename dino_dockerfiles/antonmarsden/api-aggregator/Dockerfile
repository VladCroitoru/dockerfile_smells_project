FROM node:alpine

WORKDIR /usr/src/app

COPY package*.json ./

COPY . .

RUN apk --no-cache add jq git && mkdir bin && ln -s /usr/bin/jq bin/jq && npm --unsafe-perm install --only=production && apk --no-cache del git

EXPOSE 3080

CMD [ "npm", "start" ]
