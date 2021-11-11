FROM debian:jessie AS build-env

RUN echo '\n\
deb-src http://deb.debian.org/debian jessie main\n\
deb-src http://deb.debian.org/debian jessie-updates main\n\
deb-src http://security.debian.org jessie/updates main\n'\
>> /etc/apt/sources.list

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libcrypto++-dev \
 && apt-get source -y squid3 \
 && apt-get build-dep -y squid3

COPY 99-squid3-key-usage.patch /
RUN cd squid3-* \
    && mv ../99-squid3-key-usage.patch debian/patches \
    && sed -i -e 's/DEB_CONFIGURE_EXTRA_FLAGS := /DEB_CONFIGURE_EXTRA_FLAGS := --enable-ssl --enable-ssl-crtd /' debian/rules \
    && sed -i -e '$ a 99-squid3-key-usage.patch' debian/patches/series \
    && dpkg-buildpackage -us -uc -b -j$(nproc)


FROM debian:jessie
LABEL maintainer="sumomoneko@gmail.com"

ENV SQUID_CACHE_DIR=/var/spool/squid3 \
    SQUID_LOG_DIR=/var/log/squid3 \
    SQUID_SSL_DB_DIR=/var/lib/ssl_db \
    SQUID_USER=proxy

COPY --from=build-env /*.deb /
RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    squid3 \
    libssl1.0.0 \
    python3-requests \
 && dpkg -i squid3_*.deb squid3-common_*.deb \
 && rm -f /*.deb \
 && rm -rf /var/lib/apt/lists/*

COPY squid.conf /etc/squid3/squid.conf
COPY entrypoint.sh /sbin/entrypoint.sh
RUN chmod 755 /sbin/entrypoint.sh
COPY squid_filter.py /etc/squid3/squid_filter.py
RUN chmod 755 /etc/squid3/squid_filter.py

EXPOSE 3128/tcp
VOLUME ["${SQUID_CACHE_DIR}"]
ENTRYPOINT ["/sbin/entrypoint.sh"]
