FROM alpine:3.5
MAINTAINER Nobuo OKAZAKI
RUN apk add --no-cache python2 py2-bottle bash \
 && adduser -u 1000 -D bottle bottle \
 && rm -rf /tmp/* /media /mnt /run /srv
ENV INSTALL_PREFIX=/opt/regiui
COPY ./ $INSTALL_PREFIX
RUN set -x \
 && GITREF=$(cat $INSTALL_PREFIX/.git/HEAD | cut -d" " -f2) \
 && GITSHA1=$(cat $INSTALL_PREFIX/.git/$GITREF) \
 && GITBR=$(echo refs/heads/master | cut -d/ -f3) \
 && echo "{\"git\":{\"sha1\":\"$GITSHA1\",\"branch\":\"$GITBR\"}}" > $INSTALL_PREFIX/share/regiui/static/version.json \
 && mkdir -p /var/lib/regiui \
 && chown bottle:bottle /var/lib/regiui \
 && rm -rf $INSTALL_PREFIX/.git \
 && rm -rf /tmp/* /media /mnt /run /srv \
 && python -m compileall $INSTALL_PREFIX \
 && python -O -m compileall $INSTALL_PREFIX
USER bottle
ENV PYTHONPATH=$INSTALL_PREFIX/lib \
    REGIUI_DATA_PATH=/var/lib/regiui/data
ENTRYPOINT ["bottle.py", \
  "-b", "0.0.0.0:8000", \
  "regiui:app" \
]
EXPOSE 8000
