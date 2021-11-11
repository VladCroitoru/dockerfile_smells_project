FROM alpine:3.6
MAINTAINER Chris Jones <chris@sysadminchris.com>

ENV UID=10001 UNAME=nzbget GID=10000 GNAME=media

ADD start.sh /start.sh

RUN chmod +x /start.sh \
 && addgroup -g $GID $GNAME \
 && adduser -SH -u $UID -G $GNAME -s /usr/sbin/nologin $UNAME \
 && apk add --no-cache openssl unrar p7zip python tini \
 && wget -O nzbget.run `wget -qO- http://nzbget.net/info/nzbget-version-linux.json | sed -n "s/^.*stable-download.*: \"\(.*\)\".*/\1/p"` \
 && sh nzbget.run \
 && ln -sfv /nzbget/nzbget /usr/bin/nzbget \
 && rm -rf /nzbget.run \
 && apk del --no-cache openssl

RUN mkdir /config && chown nzbget:media /config
VOLUME ["/config", "/media"]
EXPOSE 6789

USER $UNAME

ENTRYPOINT ["/sbin/tini", "--", "/start.sh"]
CMD ["nzbget", "-c", "/config/nzbget.conf", "-s", "-o", "OutputMode=log"]
