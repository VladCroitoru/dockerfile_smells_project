FROM debian:jessie

# using wget for fetching the files to avoid setting up an older version of curl for this

RUN apt-get update && apt-get install -y \
        wget ca-certificates \
        --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# build nghttp2

RUN apt-get update \
    && apt-get install -y \
        g++ make binutils autoconf automake autotools-dev libtool pkg-config \
        zlib1g-dev libcunit1-dev libssl-dev libxml2-dev libev-dev libevent-dev libjansson-dev \
        libjemalloc-dev cython python3-dev python-setuptools \
        --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* \
    && wget https://github.com/nghttp2/nghttp2/releases/download/v1.19.0/nghttp2-1.19.0.tar.gz \
    && tar -xvzf nghttp2-1.19.0.tar.gz \
    && cd nghttp2-1.19.0 \
    && autoreconf -i \
    && automake \
    && autoconf \
    && ./configure \
    && make \
    && make install \
    && cd .. \
    && rm -rf nghttp2-1.19.0 \
    && rm nghttp2-1.19.0.tar.gz \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
        autoconf automake autotools-dev binutils cpp cpp-4.9 cython dh-python file \
        g++ g++-4.9 gcc gcc-4.9 libasan1 libatomic1 libcilkrts5 libcloog-isl4 \
        libcunit1 libcunit1-dev libev-dev libev4 libevent-2.0-5 libevent-core-2.0-5 \
        libevent-dev libevent-extra-2.0-5 libevent-openssl-2.0-5 \
        libevent-pthreads-2.0-5 libexpat1 libexpat1-dev libgcc-4.9-dev libgdbm3 \
        libglib2.0-0 libgomp1 libisl10 libitm1 libjansson-dev libjansson4 \
        libjemalloc-dev libjemalloc1 liblsan0 libmagic1 libmpc3 libmpdec2 libmpfr4 \
        libpython-stdlib libpython2.7-minimal libpython2.7-stdlib libpython3-dev \
        libpython3-stdlib libpython3.4 libpython3.4-dev libpython3.4-minimal \
        libpython3.4-stdlib libquadmath0 libsigsegv2 libsqlite3-0 libstdc++-4.9-dev \
        libtool libtsan0 libubsan0 libxml2 libxml2-dev m4 make mime-support perl \
        perl-modules pkg-config python python-minimal python-pkg-resources \
        python-setuptools python2.7 python2.7-minimal python3 python3-dev \
        python3-minimal python3.4 python3.4-dev python3.4-minimal

# install libssl-dev 1.0.2 only to be found in jessie-backports for now
# then build curl

RUN echo 'deb http://ftp.debian.org/debian jessie-backports main' > /etc/apt/sources.list.d/deb-jessie-backports-main.list \
    && echo 'deb-src http://deb.debian.org/debian jessie main' > /etc/apt/sources.list.d/deb-src-jessie-main.list \
    && apt-get update \
    && apt-get -t jessie-backports install -y libssl-dev --no-install-recommends \
    && apt-get build-dep -y curl --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* \
    && wget https://curl.haxx.se/download/curl-7.52.1.tar.gz \
    && tar -xvzf curl-7.52.1.tar.gz \
    && cd curl-7.52.1 \
    && ./configure --with-nghttp2=/usr/local \
        --disable-ldap --with-ssl --disable-sspi --without-librtmp \
        --disable-dict --disable-telnet --disable-tftp --disable-rtsp \
        --disable-pop3 --disable-imap --disable-smtp --disable-gopher --disable-smb \
    && make \
    && make install \
    && ldconfig \
    && cd .. \
    && rm -rf curl-7.52.1 \
    && rm curl-7.52.1.tar.gz \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
        autoconf automake autotools-dev binutils bsdmainutils build-essential bzip2 \
        comerr-dev cpp cpp-4.9 debhelper diffstat dpkg-dev file g++ g++-4.9 gcc \
        gcc-4.9 gettext gettext-base groff-base init-system-helpers intltool-debian \
        krb5-multidev libasan1 libasprintf0c2 libatomic1 libbsd0 libcilkrts5 \
        libcloog-isl4 libcroco3 libdpkg-perl libedit2 libexpat1 libgcc-4.9-dev \
        libgcrypt20-dev libgdbm3 libglib2.0-0 libgmp-dev libgmpxx4ldbl \
        libgnutls-openssl27 libgnutls28-dev libgnutlsxx28 libgomp1 libgpg-error-dev \
        libgssapi-krb5-2 libgssrpc4 libidn11-dev libisl10 libitm1 libk5crypto3 \
        libkadm5clnt-mit9 libkadm5srv-mit9 libkdb5-7 libkeyutils1 libkrb5-3 \
        libkrb5-dev libkrb5support0 libldap-2.4-2 libldap2-dev liblsan0 libmagic1 \
        libmpc3 libmpfr4 libnspr4 libnspr4-dev libnss3 libnss3-dev libp11-kit-dev \
        libpipeline1 libpython-stdlib libpython2.7-minimal libpython2.7-stdlib \
        libquadmath0 librtmp-dev librtmp1 libsasl2-2 libsasl2-modules-db libsigsegv2 \
        libsqlite3-0 libssh2-1 libssh2-1-dev libstdc++-4.9-dev libtasn1-6-dev \
        libtimedate-perl libtool libtsan0 libubsan0 libunistring0 libwrap0 libxml2 \
        m4 make man-db mime-support nettle-dev openssh-client openssh-server \
        openssh-sftp-server patch perl perl-modules pkg-config po-debconf python \
        python-minimal python2.7 python2.7-minimal quilt stunnel4 xz-utils \
    && rm /etc/apt/sources.list.d/deb-jessie-backports-main.list \
    && rm /etc/apt/sources.list.d/deb-src-jessie-main.list \
    && apt-get update \
    && apt-get install -y libssh2-1 --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*
