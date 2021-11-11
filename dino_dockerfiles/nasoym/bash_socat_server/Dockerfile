FROM alpine:edge
MAINTAINER Sinan Goo
LABEL type="request_container"

RUN apk update && apk --no-cache add socat bash

WORKDIR /socat_server

ADD *.sh /socat_server/
ADD VERSION /socat_server/
ADD example_handlers /handlers

EXPOSE 8080

ENTRYPOINT ["./run.sh"]
CMD ["-r /handlers", "-d /handlers/default"]
