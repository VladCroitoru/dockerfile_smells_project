FROM alpine:3.5
MAINTAINER Marek Novotny <hotmana76@gmail.com>

RUN adduser -D syncthing
ADD launch.sh /launch.sh

RUN chmod +x /launch.sh && \
        apk add --no-cache --virtual libressl

ENV SYNCTHING_VERSION 0.14.24

RUN set -x \
            && tarball="syncthing-linux-arm-v${SYNCTHING_VERSION}.tar.gz" \
            && wget https://github.com/syncthing/syncthing/releases/download/v${SYNCTHING_VERSION}/${tarball} \
            && dir="$(basename "$tarball" .tar.gz)" \
            && bin="$dir/syncthing" \
            && tar -xvzf "$tarball" "$bin" \
            && rm "$tarball" \
            && mv "$bin" /usr/local/bin/syncthing \
            && rmdir "$dir"

WORKDIR /home/syncthing

VOLUME ["/home/syncthing/.config/syncthing", "/home/syncthing/Sync"]

EXPOSE 8384 22000 21027/udp

USER syncthing

CMD ["/launch.sh"]
