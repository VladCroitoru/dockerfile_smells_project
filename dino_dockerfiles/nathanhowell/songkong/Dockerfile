FROM openjdk:8-jre-alpine

RUN apk add --no-cache ca-certificates curl tini \
 && mkdir -p /opt \
 && curl http://www.jthink.net/songkong/downloads/current/songkong-linux-headless-novm.tgz?val=77 | tar -C /opt -xzf - \
 && find /opt/songkong -perm /u+x -type f -print0 | xargs -0 chmod a+x

RUN addgroup -S songkong \
 && adduser -S -G songkong songkong

USER songkong:songkong

EXPOSE 4567

ENTRYPOINT ["/sbin/tini"]

# VOLUME /opt/songkong/songkong.properties

# preferences and match database are stored here
VOLUME /home/songkong/.songkong

WORKDIR /opt/songkong

CMD /opt/songkong/songkongremote.sh

