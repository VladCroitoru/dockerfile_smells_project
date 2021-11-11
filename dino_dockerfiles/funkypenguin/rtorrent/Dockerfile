FROM phusion/baseimage:0.9.16

# BUILD_DATE and VCS_REF are immaterial, since this is a 2-stage build, but our build
# hook won't work unless we specify the args
ARG BUILD_DATE
ARG VCS_REF

# Good docker practice, plus we get microbadger badges
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/funkypenguin/rtorrent.git" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="2.2-r1"

ENV RUTORRENT_URI=https://bintray.com/artifact/download/novik65/generic/rutorrent-3.6.tar.gz\
    RUTORRENT_SHA1=5870cddef717c83560e89aee56f2b7635ed1c90d\
    RUTORRENT_PLUGINS_URI=https://bintray.com/artifact/download/novik65/generic/plugins-3.6.tar.gz\
    RUTORRENT_PLUGINS_SHA1=617625cda45c689f5505fbfdfb6cc4000bc6b1d9

RUN \
    locale-gen en_US.UTF-8 &&\
    update-locale LANG=en_US.UTF-8 &&\
    apt-get update &&\
    apt-get -y install software-properties-common &&\
    # ffmpeg ppa
    add-apt-repository -y ppa:mc3man/trusty-media &&\
    add-apt-repository -y ppa:nginx/stable &&\
	add-apt-repository -y ppa:jalaziz/rtorrent &&\
    rm -rf /var/lib/apt/lists/*


RUN \
    # install required libraries
    apt-get update &&\
    apt-get -y install\
        curl\
        ffmpeg\
        mediainfo\
        nginx\
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

#set default umask to 002
RUN rm /etc/login.defs
COPY login.defs /etc/login.defs

RUN adduser --quiet --disabled-password --home /config --gecos "" --uid 4242 htpc &&\
	usermod -g users htpc &&\
	usermod -a -G www-data htpc
	
COPY rtorrent.rc /rtorrent.rc
RUN chown -R htpc /config &&\
	chmod -R 777 /config
	
RUN mkdir /download
RUN chown -R htpc /download &&\
    chmod -R 777 /download

COPY docker-*.sh /
RUN chmod 777 /docker-*.sh
COPY rutorrent.sh /
RUN chmod 777 /rutorrent.sh
COPY ssl.sh /
RUN chmod 777 /ssl.sh
COPY edge.sh /
RUN chmod 777 /edge.sh

EXPOSE 80 443 36898 9527

VOLUME ["/config", "/download",]
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/docker-start.sh"]
