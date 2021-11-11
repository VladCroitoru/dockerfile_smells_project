FROM alpine:edge
# This is the real maintainer
# MAINTAINER Onni Hakala <onni.hakala@geniem.com>
# MAINTAINER Mickaël Perrin <dev@mickaelperrin.fr>
MAINTAINER Eugen Mayer <eugen.mayer@kontextwork.com>

ARG UNISON_VERSION=2.48.4
RUN apk add --no-cache build-base curl bash supervisor inotify-tools && \
    apk add --update-cache --repository http://dl-4.alpinelinux.org/alpine/edge/testing/ ocaml && \
    curl -L https://github.com/bcpierce00/unison/archive/$UNISON_VERSION.tar.gz | tar zxv -C /tmp && \
    cd /tmp/unison-${UNISON_VERSION} && \
    sed -i -e 's/GLIBC_SUPPORT_INOTIFY 0/GLIBC_SUPPORT_INOTIFY 1/' src/fsmonitor/linux/inotify_stubs.c && \
    make UISTYLE=text NATIVE=true STATIC=true && \
    cp src/unison src/unison-fsmonitor /usr/local/bin && \
    apk del curl build-base ocaml && \
    apk add --no-cache libgcc libstdc++ && \
    rm -rf /tmp/unison-${UNISON_VERSION}

RUN apk add --no-cache --repository http://dl-4.alpinelinux.org/alpine/edge/testing/ shadow

RUN apk add --no-cache tzdata

# These can be overridden later
ENV TZ="Europe/Helsinki" \
    LANG="C.UTF-8" \
    UNISON_DIR="/data" \
    HOME="/root"

COPY entrypoint.sh /entrypoint.sh
COPY supervisord.conf /etc/supervisord.conf
COPY supervisor.unison.conf /etc/supervisor.conf.d/supervisor.unison.conf

RUN mkdir -p /docker-entrypoint.d \
 && chmod +x /entrypoint.sh \
 && mkdir -p /etc/supervisor.conf.d

EXPOSE 5000
ENTRYPOINT ["/entrypoint.sh"]
CMD ["supervisord"]
