FROM amd64/node:current-alpine

RUN apk update && apk add bash && rm -rf /var/cache/apk/*
RUN npm install -g hackmyresume
RUN npm install handlebars

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
