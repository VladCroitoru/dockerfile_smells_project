FROM ubuntu:16.04
MAINTAINER Thiago Martins <rogue.thiago@gmail.com>

ENV DISPLAY=:0
ENV RESOLUTION=1366x768
ENV VIDEO_DIRECTORY=/data

EXPOSE 5900

WORKDIR /data

RUN apt-get -y update && \
    apt-get -y install xvfb fluxbox ffmpeg x11vnc busybox && \
    rm -rf /var/lib/apt/lists/* && \
    chown -R :users /data

ADD entrypoint.sh /
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD bash
