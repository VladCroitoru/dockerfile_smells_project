FROM ubuntu:12.04
MAINTAINER ufo28 <ufo28x50@gmail.com>

ENV LANG="en_US.UTF-8" LANGUAGE="en_US.UTF-8" APP_NAME="teamviewer9" IMG_NAME="teamviewer9" TAG_NAME="latest"
ENV DEBIAN_FRONTEND noninteractive
ENV DISPLAY :0.0

RUN echo deb http://old-releases.ubuntu.com/ubuntu/ quantal main restricted universe multiverse \
         > /etc/apt/sources.list
RUN echo exit 0 > /usr/sbin/policy-rc.d

RUN apt-get update --yes --quiet \
    && apt-get install --yes --quiet --no-install-recommends \
        sudo dbus dbus-x11 upstart curl xz-utils libc6:i386 libdbus-1-3 libasound2 libsm6 libxfixes3 \
        libdbus-1-3:i386 libasound2:i386 libexpat1:i386 libfontconfig1:i386 \
        libfreetype6:i386 libjpeg62:i386 libpng12-0:i386 libsm6:i386 \
        libxdamage1:i386 libxext6:i386 libxfixes3:i386 libxinerama1:i386 \
        libxrandr2:i386 libxrender1:i386 libxtst6:i386 zlib1g:i386 \
    && locale-gen en_US.UTF-8 \
    && dpkg-reconfigure locales \
    && curl -sLk https://dl.teamviewer.com/download/version_9x/teamviewer_linux.tar.gz -o /tmp/teamviewer_i386.tar.gz \
    && tar xf /tmp/teamviewer_i386.tar.gz -C /opt/ \
    && rm /tmp/teamviewer_i386.tar.gz \
    && apt-get remove --auto-remove --yes --purge wget \
    && apt-get clean --yes \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /usr/lib64/gconv/* \
    && rm -rf /usr/share/{man,doc,info,gnome/help} \
    && rm -rf /tmp/* \
    && rm -rf /var/log/*

VOLUME ["/opt/teamviewer9"]

COPY root /
