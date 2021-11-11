FROM alpine:3.4
MAINTAINER Seth Miller<smiller@aerisweather.com>

RUN apk update \
 && apk add --update -t addons inotify-tools \
 && rm /var/cache/apk/*

ENTRYPOINT ["inotifywait", "-m", "-e", "create", "-e", "modify", "-e", "move", "-e", "delete", "--timefmt", "%FT%TZ", "--format", "[%T] %e %w%f", "/watch"]