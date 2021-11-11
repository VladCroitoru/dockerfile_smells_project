FROM alpine:latest
MAINTAINER Lucas Servén <lserven@gmail.com>
RUN apk --update --no-cache add ca-certificates
VOLUME /cache
COPY static /static
COPY bin/keewee /
ENTRYPOINT ["/keewee"]
