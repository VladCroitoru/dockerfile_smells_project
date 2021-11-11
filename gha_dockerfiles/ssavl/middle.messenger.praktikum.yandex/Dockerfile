FROM alpine:latest

RUN apk add --no-cache --update bash nodejs npm
ADD ./ /var/www/

WORKDIR /var/www
RUN npm install && npm run build

RUN adduser -D userMain
USER userMain

EXPOSE 3000

CMD node server.js