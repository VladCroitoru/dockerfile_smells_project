FROM alpine:latest
LABEL maintainer="github.com/robertbeal"

RUN apk --no-cache add \
  curl \
  inotify-tools \
  ffmpeg \
  flac \
  libvorbis \
  libexif \
  libjpeg \
  libid3tag \
  minidlna \
  su-exec \
  && rm -rf /tmp/* \
  && mkdir /config \
  && touch /config/minidlna.conf

VOLUME /config /data
EXPOSE 8200 1900/udp

COPY entrypoint.sh /usr/local/bin
ENTRYPOINT ["entrypoint.sh"]
CMD ["-f", "/config/minidlna.conf", "-S"]
