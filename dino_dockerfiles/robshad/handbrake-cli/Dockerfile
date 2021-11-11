FROM linuxserver/baseimage
MAINTAINER Rob Shad <robertmshad@googlemail.com>
ENV APTLIST="handbrake-cli ffmpeg wget"

RUN add-apt-repository ppa:stebbins/handbrake-snapshots && \
  add-apt-repository ppa:kirillshkrogalev/ffmpeg-next

RUN apt-get update -q && \
  apt-get install $APTLIST -qy && \
  apt-get clean && rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/*

ADD init/ /etc/my_init.d/
ADD scripts/ /scripts/
RUN chmod -v +x /etc/service/*/run && \
  chmod -v +x /etc/my_init.d/*.sh

# Volumes and Ports
VOLUME ["/input", "/output", "/config"]
