FROM debian:jessie

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends \
    build-essential \
    m4 \
    ca-certificates \
    curl \
    autoconf \
    && rm -rf /var/lib/apt/lists/*

RUN curl -o /root/bison-3.0.4.tar.xz -fSL http://www.nic.funet.fi/pub/gnu/ftp.gnu.org/pub/gnu/bison/bison-3.0.4.tar.xz \
    && curl -o /root/bison-3.0.4.tar.xz.sig -fSL http://www.nic.funet.fi/pub/gnu/ftp.gnu.org/pub/gnu/bison/bison-3.0.4.tar.xz.sig \
    && gpg --keyserver keys.gnupg.net --recv-keys 78D5264E \
    && gpg --verify /root/bison-3.0.4.tar.xz.sig \
    && cd /root/ \
    && tar -xf bison-3.0.4.tar.xz \
    && cd bison-3.0.4 \
    && ./configure --disable-dependency-tracking \
    && make \
    && make install

ENV FLEX_VERSION 2.6.1

RUN curl -o /root/flex-$FLEX_VERSION.tar.gz -fSL https://github.com/westes/flex/releases/download/v$FLEX_VERSION/flex-$FLEX_VERSION.tar.gz \
    && cd /root/ \
    && tar -xf flex-$FLEX_VERSION.tar.gz \
    && cd flex-$FLEX_VERSION \
    && ./configure \
    && make \
    && make install
