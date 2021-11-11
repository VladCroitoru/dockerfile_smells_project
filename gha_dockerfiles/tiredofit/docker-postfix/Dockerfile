FROM docker.io/tiredofit/alpine:3.14
LABEL maintainer="Dave Conroy (github.com/tiredofit)"

## Set Defaults
ENV CYRUS_SASL_VERSION=2.1.27 \
    POSTSRSD_VERSION=1.11 \
    CONTAINER_ENABLE_MESSAGING=FALSE \
    CONTAINER_NAME=postfix-app

## Dependencies Setup
RUN set -x && \
    addgroup -g 2525 postfix && \
    adduser -S -D -H -h /var/spool/postfix -s /sbin/nologin -G postfix -u 2525 postfix && \
    apk update && \
    apk upgrade && \
    apk add -t .cyrus-sasl-build-deps \
                autoconf \
                automake \
                build-base \
                db-dev \
                gdbm-dev \
                git \
                gzip \
                groff \
                heimdal-dev \
                libtool \
                openldap-dev \
                openssl-dev \
                sqlite-dev \
                && \
    \
    apk add -t .postsrsd-build-deps \
                cmake \
                && \
    \
    apk add -t .postfix-run-deps \
                fail2ban \
                heimdal-libs \
                inotify-tools \
                libldap \
                openldap-clients \
                openssl \
                pflogsumm \
                postfix \
                postfix-pcre \
                postfix-ldap \
                rsyslog \
                && \
    \
    ## Build
    git clone https://github.com/roehling/postsrsd /usr/src/postsrsd && \
    cd /usr/src/postsrsd && \
    git checkout ${POSTSRSD_VERSION} && \
    mkdir build && \
    cd build && \
    mkdir -p /etc/postsrsd && \
    cmake .. -DGENERATE_SRS_SECRET=OFF \
             -DCONFIG_DIR="/etc/postsrsd" \
             -DDOC_DIR="/usr/src/postsrsd/doc" \
             -DCMAKE_INSTALL_PREFIX=/usr \
             -DINIT_FLAVOR=none \
             && \
    make && \
    make install && \
    mv /etc/postsrsd/ /assets/postsrsd && \
    \
    ## Build Cyrus SASLD
    git clone -b cyrus-sasl-${CYRUS_SASL_VERSION} https://github.com/cyrusimap/cyrus-sasl/ /usr/src/cyrus-sasl && \
    cd /usr/src/cyrus-sasl && \
    wget https://git.alpinelinux.org/aports/plain/main/cyrus-sasl/CVE-2019-19906.patch && \
    wget https://git.alpinelinux.org/aports/plain/main/cyrus-sasl/cyrus-sasl-2.1.27-as_needed.patch && \
    wget https://git.alpinelinux.org/aports/plain/main/cyrus-sasl/cyrus-sasl-2.1.27-avoid_pic_overwrite.patch && \
    wget https://git.alpinelinux.org/aports/plain/main/cyrus-sasl/cyrus-sasl-2.1.27-doc_build_fix.patch && \
    wget https://git.alpinelinux.org/aports/plain/main/cyrus-sasl/cyrus-sasl-2.1.27-gss_c_nt_hostbased_service.patch && \
    wget https://git.alpinelinux.org/aports/plain/main/cyrus-sasl/autoconf-270.patch && \
    wget https://git.alpinelinux.org/aports/plain/main/cyrus-sasl/fix-saslauthd-man-page.patch && \
    for patch in ./*.patch; do echo "** Applying $patch"; patch -p1 < $patch; done && \
    autoreconf -fiv && \
    ./configure \
        --prefix=/usr \
        --sysconfdir=/etc \
        --localstatedir=/var \
        --mandir=/usr/src/cyrus-sasl/man \
        --disable-java \
        --disable-otp \
        --enable-alwaystrue \
        --enable-anon \
        --enable-auth-sasldb \
        --enable-cram \
        --enable-digest \
        --enable-gssapi \
        --enable-ldapdb \
        --enable-login \
        --enable-ntlm \
        --enable-plain \
        --enable-shared \
        --enable-static \
        --with-configdir=/etc/sasl2 \
        --with-dblib=gdbm \
        --with-dbpath=/etc/sasl2/sasldb2 \
        --with-devrandom=/dev/urandom \
        --with-gss_impl=heimdal \
        --with-ldap=/usr \
        --with-plugindir=/usr/lib/sasl2 \
        --with-rc4 \
        --with-saslauthd=/run/saslauthd \
        --without-pwcheck \
        && \
    \
    make -j$(getconf _NPROCESSORS_ONLN) && \
    make install && \
    mkdir -p /etc/sasl2/sasldb2 && \
    ln -s /etc/postfix/aliases /etc/aliases && \
    \
    ## Cleanup
    cd /etc/fail2ban && \
    rm -rf fail2ban.conf fail2ban.d jail.conf jail.d paths-*.conf && \
    apk del .cyrus-sasl-build-deps .postsrsd-build-deps && \
    rm -rf /usr/src/* && \
    rm -rf /etc/logrotate.d/rsyslog && \
    rm -rf /var/cache/apk/*

## Networking Configuration
EXPOSE 25 587

## Entrypoint Configuration
ADD install /
