FROM alpine:3.5
ENTRYPOINT ["/bin/logspout"]
VOLUME /mnt/routes
EXPOSE 80

COPY . /src
RUN cd /src && ./build.sh "$(cat VERSION)"

# Add the CA Certiciate
# https://github.com/gliderlabs/logspout/issues/147
RUN apk add -U --virtual build-dependencies curl ca-certificates \
  && curl https://logdog.loggly.com/media/logs-01.loggly.com_sha12.crt -o /usr/local/share/ca-certificates/loggly.crt \
  && update-ca-certificates \
  && apk del build-dependencies \
  && rm -rf /var/cache/apk/*

ONBUILD COPY ./build.sh /src/build.sh
ONBUILD COPY ./modules.go /src/modules.go
ONBUILD RUN cd /src && ./build.sh "$(cat VERSION)-custom"

