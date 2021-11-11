FROM phusion/baseimage:0.9.16

ENV RUTORRENT_URI=https://bintray.com/artifact/download/novik65/generic/rutorrent-3.6.tar.gz\
    RUTORRENT_SHA1=5870cddef717c83560e89aee56f2b7635ed1c90d\
    RUTORRENT_PLUGINS_URI=https://bintray.com/artifact/download/novik65/generic/plugins-3.6.tar.gz\
    RUTORRENT_PLUGINS_SHA1=617625cda45c689f5505fbfdfb6cc4000bc6b1d9

ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV TERM xterm

RUN \
    locale-gen en_US.UTF-8 &&\
    update-locale LANG=en_US.UTF-8 &&\
    apt-get update &&\
    apt-get -y install software-properties-common &&\
    # ffmpeg ppa
    add-apt-repository -y ppa:mc3man/trusty-media &&\
    add-apt-repository -y ppa:nginx/stable &&\
	add-apt-repository -y ppa:nathan-renniewaldock/ppa &&\
    rm -rf /var/lib/apt/lists/*


RUN \
    # install required libraries
    apt-get update &&\
    apt-get -y install\
        curl\
        ffmpeg\
        mediainfo\
        nginx\
        mc \
        php5-cli\
        php5-fpm\
        php5-geoip\
        rtorrent\
        tmux\
        unrar-free\
        unzip\
        git\
		wget &&\
    rm -rf /var/lib/apt/lists/*

# grab gosu for easy step-down from root
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4
RUN curl -o /usr/local/bin/gosu -SL "https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-architecture)" \
    && curl -o /usr/local/bin/gosu.asc -SL "https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-architecture).asc" \
    && gpg --verify /usr/local/bin/gosu.asc \
    && rm /usr/local/bin/gosu.asc \
    && chmod +x /usr/local/bin/gosu

COPY config.php /config.php
COPY htpasswd /htpasswd

RUN mkdir /config

RUN \
    cd /var/www &&\
    # install rutorrent
    wget -q -O rutorrent.tar.gz $RUTORRENT_URI &&\
    echo "$RUTORRENT_SHA1  rutorrent.tar.gz" | sha1sum -c - &&\
    tar -xf rutorrent.tar.gz &&\
    rm rutorrent.tar.gz &&\
    # install rutorrent plugins
    cd rutorrent &&\
    wget -q -O plugins.tar.gz $RUTORRENT_PLUGINS_URI &&\
    echo "$RUTORRENT_PLUGINS_SHA1  plugins.tar.gz" | sha1sum -c - &&\
    tar xf plugins.tar.gz &&\
    rm plugins.tar.gz &&\	
	rm /var/www/rutorrent/conf/config.php &&\
	cp /config.php /var/www/rutorrent/conf/config.php &&\
	# correct files permission
    chmod -R 777 /var/www &&\
    chown -R www-data. /var/www

# remove default nginx config
RUN rm /etc/nginx/sites-available/* &&\
    rm /etc/nginx/sites-enabled/*
# add nginx config for rutorrent
COPY nginx /etc/nginx
RUN ln -s /etc/nginx/sites-available/rutorrent /etc/nginx/sites-enabled/rutorrent

# copy php.ini
RUN rm /etc/php5/fpm/php.ini
COPY php.ini /etc/php5/fpm/php.ini


#set default umask to 002
RUN rm /etc/login.defs
COPY login.defs /etc/login.defs

RUN adduser --quiet --disabled-password --home /config --gecos "" --uid 1000 torrent &&\
	usermod -g users torrent &&\
	usermod -a -G www-data torrent
	
COPY rtorrent.rc /rtorrent.rc
RUN chown -R torrent /config &&\
	chmod -R 777 /config
	
RUN mkdir /download
RUN mkdir /downloadwatch
RUN mkdir /downloadunraid

RUN chown -R torrent /download 
RUN chown -R torrent /downloadwatch 

RUN chmod -R 777 /download
RUN chmod -R 777 /downloadunraid
RUN chmod -R 777 /downloadwatch

COPY docker-*.sh /
RUN chmod 777 /docker-*.sh
COPY rutorrent.sh /
RUN chmod 777 /rutorrent.sh
COPY ssl.sh /
RUN chmod 777 /ssl.sh
COPY edge.sh /
RUN chmod 777 /edge.sh

COPY favicon.ico /

EXPOSE 80 443 45566-45576 9527

VOLUME ["/config", "/download", "/downloadunraid"]
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/docker-start.sh"]
