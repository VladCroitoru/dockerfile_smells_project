FROM alpine:latest
MAINTAINER Tim van Dijk
ARG GITTAG=2.1.0
ARG PAR2TAG=v0.6.14 

RUN buildDeps="gcc g++ git mercurial make automake autoconf python-dev openssl-dev libffi-dev musl-dev" \
  && apk --update add $buildDeps \
  && apk add \
    python \
    py2-pip py2-openssl \
    ffmpeg-libs \
    ffmpeg \
    unrar \
    openssl \
    ca-certificates \
    p7zip \
&& pip install --upgrade pip --no-cache-dir \
&& pip install cheetah --no-cache-dir \
&& pip install sabyenc --upgrade \
&& git clone --depth 1 --branch ${PAR2TAG} https://github.com/Parchive/par2cmdline.git \
&& cd /par2cmdline \
&& aclocal \
&& automake --add-missing \
&& autoconf \
&& ./configure \
&& make \
&& make install \
&& cd / \
&& rm -rf par2cmdline \
&& git clone --depth 1 --branch ${GITTAG} https://github.com/sabnzbd/sabnzbd.git \
&& cd / \
&& echo '#!/bin/sh' > /start \
&& echo '[ -z "$UID" ] && UID=0' >> /start \
&& echo '[ -z "$GID" ] && GID=0' >> /start \
&& echo 'echo -e "appuser:x:${UID}:${GID}:appuser:/app:/bin/false\n" >> /etc/passwd' >> /start \
&& echo 'echo -e "appgroup:x:${GID}:appuser\n" >> /etc/group' >> /start \
&& echo 'mkdir -p /config' >> /start \
&& echo 'mkdir -p /data' >> /start \
&& echo 'chown -R appuser:appgroup /config' >> /start \
&& echo 'chown appuser:appgroup /data' >> /start \
&& echo 'exec /bin/su -p -s "/bin/sh" -c "exec ./SABnzbd.py -b 0 -f /config/ -s 0.0.0.0:8080" appuser' >> /start \
&& chmod +x /start \
&& rm -rf /yenc \
&& apk del $buildDeps \
&& rm -rf \
    /var/cache/apk/* \
    /par2cmdline \
    /yenc \
    /sabnzbd/.git \
    /tmp/*

EXPOSE 8080 9090

VOLUME ["/config", "/data"]

WORKDIR /sabnzbd

CMD ["/start"]


