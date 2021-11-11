FROM selenoid/video-recorder:latest

RUN apk add -U x264-libs sdl2 libxcb libbz2 xset && \
    rm -rf /var/cache/apk/* && rm /entrypoint.sh

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
