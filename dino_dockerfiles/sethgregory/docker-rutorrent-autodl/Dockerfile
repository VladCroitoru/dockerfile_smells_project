FROM linuxserver/baseimage.nginx

MAINTAINER Seth Gregory <sethgregory@gmail.com>

ENV BUILD_APTLIST="autoconf automake build-essential make pkg-config swig3.0 tcl8.6-dev python3-dev libicu-dev libperl-dev libpython3-dev libsasl2-dev libssl-dev libxml2-dev libncurses5-dev"
ENV APTLIST="dtach ffmpeg git-core mediainfo nano php5-geoip rtorrent unrar unzip wget irssi"

# install packages
RUN echo "deb http://archive.ubuntu.com/ubuntu/ trusty-backports main restricted universe multiverse" >> /etc/apt/sources.list && \
echo "deb-src http://archive.ubuntu.com/ubuntu/ trusty-backports main restricted universe multiverse" >> /etc/apt/sources.list && \
add-apt-repository ppa:kirillshkrogalev/ffmpeg-next && \
add-apt-repository -y ppa:jalaziz/rtorrent && \
apt-get update -q && \
apt-get install \
$BUILD_APTLIST \
$APTLIST -qy && \

# cleanup
apt-get clean -y && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#Adding Custom files
ADD defaults/ /defaults/
ADD init/ /etc/my_init.d/
ADD services/ /etc/service/
RUN chmod -v +x /etc/service/*/run /etc/my_init.d/*.sh && \

# configure php
sed -i 's#;upload_tmp_dir =#upload_tmp_dir = /config/tmp#g' /etc/php5/fpm/php.ini

# ports and volumes
EXPOSE 80 9527/udp 45566-45576
VOLUME /config /downloads
