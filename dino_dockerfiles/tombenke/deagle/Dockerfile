FROM ubuntu:16.04

ENV HOME /home/developer
ENV EAGLEDIR=/home/developer/topics/eagle
ENV QT_XKB_CONFIG_ROOT=/usr/share/X11/xkb

WORKDIR /home/developer

# Replace 1000 with your user / group id
RUN export uid=1000 gid=1000 && \
    mkdir -p /home/developer && \
    mkdir -p /etc/sudoers.d && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer && \
    chown ${uid}:${gid} -R /home/developer && \
    apt-get update && \
    apt-get install -y \
        wget \
        sudo \
        bzip2 \
        libxrender1 \
        libxrandr2 \
        libxcursor1 \
        libxi6 \
        libssl1.0.0 \
        libfontconfig \
        libfreetype6 \
        libcups2 \
        libx11-xcb1 && \
    wget ftp://ftp.cadsoft.de/eagle/program/7.7/eagle-lin64-7.7.0.run && \
    chmod ug+xs eagle-lin64-7.7.0.run

USER developer


