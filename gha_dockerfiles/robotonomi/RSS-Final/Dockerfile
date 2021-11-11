FROM alpine:3.10

RUN apk update \
 && apk add jq curl gettext perl

COPY entrypoint.sh /entrypoint.sh

RUN chmod 755 /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
