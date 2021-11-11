FROM alpine
RUN apk update && apk add drill
COPY ./watchdns /usr/local/bin/watchdns
ENV HOME /run
ENTRYPOINT ["watchdns"]
