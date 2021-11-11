FROM alpine:edge
LABEL maintainer Kenzo Okuda <kyokuheki@gmail.com>

RUN apk add --no-cache clamav clamav-daemon clamav-libunrar freshclam runit

RUN mkdir -p /etc/sv/clamd /etc/sv/freshclam \
 && echo -e '#!/bin/sh\n exec 1>&2 clamd\n' > /etc/sv/clamd/run \
 && echo -e '#!/bin/sh\n exec 1>&2 freshclam -d --stdout -v -c1' > /etc/sv/freshclam/run \
 && chmod +x /etc/sv/clamd/run /etc/sv/freshclam/run

COPY *.conf /etc/clamav/
#COPY clamd /etc/sv/clamd/run
#COPY freshclam /etc/sv/freshclam/run

VOLUME ["/var/lib/clamav"]
EXPOSE 3310
ENTRYPOINT []
CMD set -ex; \
    freshclam --stdout -v || true; \
    exec /sbin/runsvdir /etc/sv

HEALTHCHECK --start-period=350s --interval=60s --timeout=5s \
 CMD [ "$(echo PING | nc localhost 3310)" = "PONG" ] || exit 1
