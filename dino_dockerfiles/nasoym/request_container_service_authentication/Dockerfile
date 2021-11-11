FROM alpine:edge
MAINTAINER Sinan Goo

RUN apk update && apk upgrade
RUN apk --no-cache add socat bash curl sed jq openssl

WORKDIR /socat_server

ADD *.sh /socat_server/
ADD lib /socat_server/lib

RUN mkdir /socat_server/logs
RUN touch /socat_server/logs/logs

EXPOSE 8080

ENTRYPOINT ["./run.sh"]


