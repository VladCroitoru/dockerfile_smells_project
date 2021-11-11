FROM node:alpine

WORKDIR /app/

COPY . /app/

ENV NODE_ENV production

RUN apk update && apk add --no-cache git bash

RUN npm install --production
RUN npm run build

ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh .
RUN chmod +x wait-for-it.sh

ENTRYPOINT /app/entrypoint.sh
