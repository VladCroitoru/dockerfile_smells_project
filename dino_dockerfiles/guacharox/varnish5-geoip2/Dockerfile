FROM debian:jessie-slim

RUN apt-get update && apt-get install curl git -y
RUN curl -s https://packagecloud.io/install/repositories/varnishcache/varnish5/script.deb.sh | bash
RUN apt-get install  varnish=5.1.2-1 varnish-dev=5.1.2-1 -y
RUN apt-get install autoconf automake pkg-config libtool make python-docutils -y \
    && mkdir /opt/maxmind \
    && git clone --recursive https://github.com/maxmind/libmaxminddb /opt/maxmind \
    && cd /opt/maxmind \
    && ./bootstrap \
    && ./configure \
    && make \
    && make install \
    && ldconfig \
    && sh -c "echo /usr/local/lib  >> /etc/ld.so.conf.d/local.conf" \
    && ldconfig \ 
    && export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig \
    && mkdir /opt/libvmod-geoip2 \
    && git clone --recursive https://github.com/fgsch/libvmod-geoip2 /opt/libvmod-geoip2 \
    && cd /opt/libvmod-geoip2  \
    && ./autogen.sh \
    && ./configure  \
    && make \
    && make install \
    && apt-get remove curl -y \
    && dpkg -r git && apt-get autoremove -y \ 
    && apt-get purge -y $(dpkg --list |grep '^rc' |awk '{print $2}')

