FROM alpine:3.4
MAINTAINER Garrett Heaver <https://github.com/garrettheaver>

# bootstrap pkgs
RUN apk update \
  && apk add ca-certificates git

# essential files
COPY ./entrypoint.sh /bin
COPY ./ssh.config /etc/ssh/config

ENTRYPOINT ["/bin/entrypoint.sh"]

