## Dockerfile
## https://docker.github.io/engine/reference/builder/

FROM alpine:3
RUN set -eux; \
  apk --no-cache add -X http://dl-cdn.alpinelinux.org/alpine/edge/testing gosu \
  && apk --no-cache add supervisor tor haproxy

ADD entrypoint.sh /opt/entrypoint.sh
RUN set -eux; \
  chmod +x /opt/entrypoint.sh

ENTRYPOINT [ "/opt/entrypoint.sh" ]
CMD [ ]
