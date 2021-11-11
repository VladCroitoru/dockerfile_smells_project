FROM alpine:3.5
MAINTAINER Roman Gorodyshcher "roman.gorodischer@gmail.com"

COPY take_snapshot.sh apply_snapshot.sh /usr/

RUN mkdir -p /data/snapshot \
    && mkdir /data/active \
    && chmod +x /usr/take_snapshot.sh \
    && chmod +x /usr/apply_snapshot.sh

