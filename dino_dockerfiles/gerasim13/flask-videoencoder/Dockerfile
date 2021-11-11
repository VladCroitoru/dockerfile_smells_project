FROM gerasim13/flask-gunicorn
COPY requirements.txt /tmp/

ENV FFMPEG_VERSION=3.0
RUN apk add --update build-base g++ curl nasm tar git bzip2 zlib-dev openssl-dev yasm-dev lame-dev libogg-dev && \
  x264-dev libvpx-dev libvorbis-dev x265-dev freetype-dev libass-dev libwebp-dev rtmpdump-dev libtheora-dev && \
  opus-dev python3-dev sqlite sqlite-libs sqlite-dev && \
  DIR=$(mktemp -d) && cd ${DIR} && \
  curl -s http://ffmpeg.org/releases/ffmpeg-${FFMPEG_VERSION}.tar.gz | tar zxvf - -C . && \
  cd ffmpeg-${FFMPEG_VERSION} && \
  ./configure \
  --enable-version3 --enable-gpl --enable-nonfree --enable-small --enable-libmp3lame --enable-libx264 --enable-libx265 --enable-libvpx --enable-libtheora --enable-libvorbis --enable-libopus --enable-libass --enable-libwebp --enable-librtmp --enable-postproc --enable-avresample --enable-libfreetype --enable-openssl --disable-debug && \
  make && \
  make install && \
  make distclean && \
  rm -rf ${DIR} && \
  pip3 install -r /tmp/requirements.txt && \
  apk del build-base curl tar bzip2 x264 openssl nasm python3-dev sqlite-dev && \
  rm -rf /var/cache/apk/* && \
  rm -rf /root/.cache/pip/* && \
  rm -rf /var/cache/apk/* && \
  rm -rf /tmp/*
