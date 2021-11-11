FROM alpine:latest
MAINTAINER Michael Campbell <michael.campbell@gmail.com>

RUN apk update && apk add perl ack
CMD ["--help"]
ENTRYPOINT ["/usr/bin/ack"]
