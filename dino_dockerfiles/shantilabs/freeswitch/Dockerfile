# based on https://github.com/BetterVoice/freeswitch-container
FROM ubuntu:14.04

ENV FREESWITCH_USER=freeswitch \
    FREESWITCH_VERSION=1.6.7 \
    FREESWITCH_LOGDIR=/usr/local/freeswitch/log

# Install Dependencies.
RUN set -x \
    && echo "deb http://us.archive.ubuntu.com/ubuntu/ trusty multiverse" >> /etc/apt/source.list \
    && echo "deb-src http://us.archive.ubuntu.com/ubuntu/ trusty multiverse" >> /etc/apt/source.list \
    && echo "deb http://us.archive.ubuntu.com/ubuntu/ trusty-updates multiverse" >> /etc/apt/source.list \
    && echo "deb-src http://us.archive.ubuntu.com/ubuntu/ trusty-updates multiverse" >> /etc/apt/source.list \
    && apt-get update \
    && apt-get install -y \
        autoconf \
        automake \
        bison \
        fail2ban \
        g++ \
        gawk \
        git \
        ladspa-sdk-dev \
        libasound-dev \
        libasound2-dev \
        libcurl4-openssl-dev \
        libdb-dev \
        libedit-dev \
        libexpat1-dev \
        libgdbm-dev \
        libldns-dev \
        libmemcached-dev \
        libmp3lame-dev \
        libncurses-dev \
        libogg-dev \
        libpcre3-dev \
        libperl-dev \
        libpq-dev \
        libspeex-dev \
        libspeexdsp-dev \
        libsqlite3-dev \
        libssl-dev \
        libtiff4-dev \
        libvorbis-dev \
        libx11-dev \
        libzrtpcpp-dev \
        make \
        nasm \
        portaudio19-dev \
        python-dev \
        snmpd \
        subversion \
        unixodbc-dev \
        uuid-dev \
        wget \
        yasm \
        zlib1g-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get purge -y \
    \
    && ln -sf /usr/bin/gawk /usr/bin/awk \
    \
    && touch /etc/ld.so.conf.d/x86_64-linux-freeswitch.conf \
    && echo "/usr/local/lib" >> /etc/ld.so.conf.d/x86_64-linux-freeswitch.conf \
    \
    && export LIBSHOUT_VERSION=2.3.1 \
    && cd /usr/src \
    && wget http://downloads.xiph.org/releases/libshout/libshout-$LIBSHOUT_VERSION.tar.gz \
    && tar -xzvf libshout-$LIBSHOUT_VERSION.tar.gz \
    && rm libshout-$LIBSHOUT_VERSION.tar.gz \
    && cd libshout-$LIBSHOUT_VERSION \
    && ./configure \
        --enable-shared \
        --prefix=/usr/local \
    && make \
    && make install \
    && echo "for mod_shout" \
    \
    && export MPG123_VERSION=1.22.2 \
    && cd /usr/src \
    && svn checkout svn://scm.orgis.org/mpg123/tags/$MPG123_VERSION mpg123-$MPG123_VERSION \
    && cd mpg123-$MPG123_VERSION \
    && autoreconf -iv \
    && ./configure \
        --enable-shared \
        --prefix=/usr/local \
    && make \
    && make install \
    \
    && echo "for mod_sndfile" \
    && export LIBSNDFILE_VERSION=1.0.25 \
    && cd /usr/src \
    && wget http://www.mega-nerd.com/libsndfile/files/libsndfile-$LIBSNDFILE_VERSION.tar.gz \
    && tar -xzvf libsndfile-$LIBSNDFILE_VERSION.tar.gz \
    && rm libsndfile-$LIBSNDFILE_VERSION.tar.gz \
    && cd libsndfile-$LIBSNDFILE_VERSION \
    && ./configure \
        --enable-shared \
        --prefix=/usr/local \
    && make \
    && make install \
    \
    && echo "for mod_soundtouch" \
    && export SOUNDTOUCH_VERSION=1.9.0 \
    && cd /usr/src \
    && wget http://www.surina.net/soundtouch/soundtouch-$SOUNDTOUCH_VERSION.tar.gz \
    && tar -xzvf soundtouch-$SOUNDTOUCH_VERSION.tar.gz \
    && rm soundtouch-$SOUNDTOUCH_VERSION.tar.gz \
    && cd soundtouch \
    && ./bootstrap \
    && ./configure \
        --enable-shared \
        --prefix=/usr/local \
    && make \
    && make install \
    \
    && ldconfig

COPY conf/freeswitch.conf /etc/fail2ban/filter.d/freeswitch.conf
COPY conf/freeswitch-dos.conf /etc/fail2ban/filter.d/freeswitch-dos.conf
COPY conf/jail.local /etc/fail2ban/jail.local

RUN cd /usr/src \
    && GIT_SSL_NO_VERIFY=1 git clone https://freeswitch.org/stash/scm/fs/freeswitch.git \
        -b v$FREESWITCH_VERSION \
        --depth=1 \
    && cd freeswitch \
    && ./bootstrap.sh

COPY modules.conf /usr/src/freeswitch/modules.conf

RUN cd /usr/src/freeswitch \
    && ./configure \
        --enable-64 \
        --enable-core-pgsql-support  \
        --enable-optimization \
    && make \
    && make install \
    && make uhd-sounds-install \
    && make uhd-moh-install \
    && make samples

COPY sysv/init /etc/init.d/freeswitch
COPY sysv/default /etc/default/freeswitch

RUN chmod +x /etc/init.d/freeswitch \
    && update-rc.d -f freeswitch defaults \
    && adduser \
        --gecos "FreeSWITCH Voice Platform" \
        --no-create-home \
        --disabled-login \
        --disabled-password \
        --system \
        --ingroup daemon \
        --home /usr/local/freeswitch \
        $FREESWITCH_USER \
    && chown -R $FREESWITCH_USER:daemon /usr/local/freeswitch \
    && touch $FREESWITCH_LOGDIR/freeswitch.log \
    && chown $FREESWITCH_USER:daemon $FREESWITCH_LOGDIR/freeswitch.log

VOLUME [ "$FREESWITCH_LOGDIR" ]

# for SIP signal trafic 5998 for internal interface and 5080 for external providers
EXPOSE 5998/udp 5080/udp
EXPOSE 8021/tcp
EXPOSE 64535-65535/udp

USER $FREESWITCH_USER

CMD service snmpd start \
    && service freeswitch start \
    && tail -f $FREESWITCH_LOGDIR/freeswitch.log
