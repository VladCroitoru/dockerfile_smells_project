# MotionEye

FROM ubuntu:18.04

LABEL maintainer="malvarez00@icloud.com"
ARG VERSION=0.42

# Environment Settings
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get --quiet --yes update

RUN apt-get --quiet --yes install motion \
                                  ffmpeg \
                                  v4l-utils

RUN apt-get --quiet --yes install python-pip \
                                  python-dev \
                                  curl \
                                  libssl-dev \
                                  libcurl4-openssl-dev \
                                  libjpeg-dev

# RUN pip install --upgrade pip
RUN pip install motioneye

RUN apt-get --quiet autoremove --yes && \
    apt-get --quiet --yes clean

# Prepare the configuration directory
RUN mkdir -p /etc/motioneye
RUN cp /usr/local/share/motioneye/extra/motioneye.conf.sample /etc/motioneye/motioneye.conf

# Prepare the media directory
RUN mkdir -p /var/lib/motioneye

CMD /usr/local/bin/meyectl startserver -c /etc/motioneye/motioneye.conf

# R/W needed for motioneye to update configurations; Video & Images
VOLUME ["/etc/motioneye", "/var/lib/motioneye"]

EXPOSE 8765
