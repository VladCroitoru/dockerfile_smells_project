FROM alpine:edge
MAINTAINER Sinan Goo

RUN apk update && apk upgrade
RUN apk --no-cache add socat bash curl sed

WORKDIR /socat_server

ADD *.sh /socat_server/
ADD lib /socat_server/lib

EXPOSE 8080

ENTRYPOINT ["./run.sh"]

