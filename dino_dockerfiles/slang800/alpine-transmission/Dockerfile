FROM alpine:latest
MAINTAINER Sean Lang <slang800@gmail.com>
VOLUME ["/blocklists", "/downloads", "/incomplete", "/resume", "/torrents", "/watch"]
RUN apk add --no-cache transmission-daemon && \
    mkdir -p /root/.config/transmission-daemon/ && \
    ln -f -s /blocklists /resume /torrents /root/.config/transmission-daemon/
COPY settings.json /root/.config/transmission-daemon/settings.json
EXPOSE 9091 51413/tcp 51413/udp
ENTRYPOINT ["/usr/bin/transmission-daemon", "--foreground", \
            "--download-dir", "/downloads", \
            "--incomplete-dir", "/incomplete", \
            "--watch-dir", "/watch"]
