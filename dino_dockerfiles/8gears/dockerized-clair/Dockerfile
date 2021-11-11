FROM quay.io/coreos/clair:v2.0.1 as clair  

# ADD Dockerize 
FROM alpine as build 
RUN apk add --no-cache curl ca-certificates
RUN curl -sL https://github.com/jwilder/dockerize/releases/download/v0.5.0/dockerize-alpine-linux-amd64-v0.5.0.tar.gz | tar zxf - -C /tmp

# Resulting Image
FROM alpine
RUN apk add --no-cache git bzr rpm xz
COPY --from=clair /clair /usr/local/bin/clair
COPY --from=build /tmp/dockerize /usr/local/bin/dockerize
ADD config.tpl.yaml /etc/clair/config.tpl.yaml
EXPOSE 6060 6061
VOLUME /tmp
CMD dockerize -template /etc/clair/config.tpl.yaml:/etc/clair/config.yaml -wait tcp://${DB_HOST}:${DB_PORT} -timeout 60s clair