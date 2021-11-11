FROM alpine

MAINTAINER Brian Lycett <brian@wheelybird.com?

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod a+x /usr/local/bin/entrypoint.sh

RUN apk update && apk add openvpn
ENTRYPOINT ["entrypoint.sh"]
