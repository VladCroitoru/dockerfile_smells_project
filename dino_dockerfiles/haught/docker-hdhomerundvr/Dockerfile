
FROM alpine:latest
LABEL Maintainer="Matt Haught <matt@haught.org>" \
  version="1.0" \
  description="HD HomeRun DVR"

RUN apk add --no-cache curl

RUN adduser --system --no-create-home --uid 65002 homerun

COPY hdhomerun.conf /opt/hdhomerun/etc/
COPY run-dvr.sh /run-dvr.sh

RUN mkdir -p /opt/hdhomerun \
             /opt/hdhomerun/bin \
             /opt/hdhomerun/etc \
    && mkdir /data \
    && chown -R homerun /data \
    && touch /opt/hdhomerun/bin/hdhomerun_record \
    && chmod -v +x /opt/hdhomerun/bin/hdhomerun_record \
    && chown homerun /opt/hdhomerun/bin/hdhomerun_record \
    && chown -R homerun /opt/hdhomerun \
    && chmod -v +x /run-dvr.sh

EXPOSE 65001/udp 65002

VOLUME ["/data"]

USER 65002

CMD ["/run-dvr.sh"]
