FROM alpine:latest

 RUN   apk update \
  &&   apk add ca-certificates wget bash \
  &&   update-ca-certificates

RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.25-r0/glibc-2.25-r0.apk
RUN apk add glibc-2.25-r0.apk

RUN mkdir /tmp/app
ADD ./WeatherApp/bin/ /tmp/app/WeatherApp/bin
ADD ./docker-start.sh /tmp/app
RUN chmod 755 /tmp/app/WeatherApp/bin/WeatherApp

USER root

EXPOSE 8099
ENTRYPOINT ["/tmp/app/docker-start.sh"]
