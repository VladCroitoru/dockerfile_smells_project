FROM ubuntu:14.04

ARG RUTORRENT_URI='https://bintray.com/artifact/download/novik65/generic/ruTorrent-3.7.zip'
ARG RUTORRENT_SHA1='4be55a9038ae9c9eb6052cb65ed6139a591a49a2'

RUN locale-gen en_US.UTF-8 \
    && update-locale LANG=en_US.UTF-8 \
    && apt-get update \
    && apt-get -y install software-properties-common \
    # ffmpeg ppa
    && add-apt-repository -y ppa:mc3man/trusty-media \
    && add-apt-repository -y ppa:nginx/stable \
    && rm -rf /var/lib/apt/lists/*


# install required libraries
RUN apt-get update \
    && apt-get -y install \
        curl \
        ffmpeg \
        mediainfo \
        nginx \
        php5-cli \
        php5-fpm \
        php5-geoip \
        rtorrent \
        tmux \
        unrar-free \
        unzip \
        wget \
    # remove default sites
    && rm /etc/nginx/sites-available/* /etc/nginx/sites-enabled/* \
    && rm -rf /var/lib/apt/lists/*

# copy nginx config
COPY nginx-rutorrent /etc/nginx/sites-enabled/rutorrent

# grab gosu for easy step-down from root
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
    && curl -o /usr/local/bin/gosu -SL "https://github.com/tianon/gosu/releases/download/1.9/gosu-$(dpkg --print-architecture)" \
    && curl -o /usr/local/bin/gosu.asc -SL "https://github.com/tianon/gosu/releases/download/1.9/gosu-$(dpkg --print-architecture).asc" \
    && gpg --verify /usr/local/bin/gosu.asc \
    && rm /usr/local/bin/gosu.asc \
    && chmod +x /usr/local/bin/gosu

RUN cd /var/www \
    # install rutorrent
    && wget -qO rutorrent.zip $RUTORRENT_URI \
    && echo "$RUTORRENT_SHA1  rutorrent.zip" | sha1sum -c - \
    && unzip rutorrent.zip \
    && mv ruTorrent-master rutorrent \
    && rm rutorrent.zip \
    # correct files permission
    && chmod -R 755 /var/www \
    # fix curl not found
    && sed -i 's#\(\s*"curl"\s*=>\s*'"'"'\)''\('"'"'.*\)#\1/usr/bin/curl\2#g' /var/www/rutorrent/conf/config.php \
    && chown -R www-data. /var/www

RUN mkdir /torrent \
    && adduser --quiet --disabled-password --home /torrent/home --gecos "" --uid 1000 torrent

COPY rtorrent.rc /torrent/home/.rtorrent.rc
RUN cd /torrent \
    && mkdir download watch home/.rtorrentsession \
    && chown -R torrent. /torrent \
    && chgrp www-data home/.rtorrentsession

COPY docker-* rutorrent.sh /

VOLUME ["/torrent/home", "/torrent/download", "/torrent/watch"]
ENTRYPOINT ["/docker-entrypoint"]
CMD ["/docker-start"]

