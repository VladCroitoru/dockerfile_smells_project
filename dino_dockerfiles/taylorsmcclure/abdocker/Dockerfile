FROM alpine:edge
MAINTAINER Taylor McClure github.com/taylorsmcclure

RUN apk update \
    && apk add --no-cache --virtual temp-pkgs g++ make git \
    && apk add --no-cache python2=2.7.12-r3 nodejs=6.5.0-r0 \
    && npm install npm -g \
    && addgroup -S awesomebot \
    && adduser -h /awesomebot -s /sbin/nologin -S awesomebot -g awesomebot \
    && npm init --yes \
    && npm i https://github.com/BitQuote/AwesomeBot.git \
    && chown -R awesomebot:awesomebot /node_modules \
    && apk del --purge temp-pkgs

USER awesomebot
WORKDIR "/node_modules/AwesomeBot"
EXPOSE 8080
ENTRYPOINT ["/usr/bin/node", "bot.js"]
