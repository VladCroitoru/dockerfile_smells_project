#
# Socle d'exécution de strass
#

FROM debian:stretch-slim

RUN set -ex; \
    apt-get update -y ; \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        apt-transport-https lsb-release ca-certificates curl gnupg \
        ; \
    curl https://packages.sury.org/php/apt.gpg | apt-key add - ; \
    echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" > /etc/apt/sources.list.d/php.list ; \
    apt-get update -y ; \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        ghostscript \
        locales \
        make \
        php5.6-fpm \
        php5.6-gd \
        php5.6-mbstring \
        php5.6-opcache \
        php5.6-sqlite3 \
        rsync \
        sudo \
        ; \
    DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -y --no-install-recommends ; \
    apt-get clean ; \
    rm -rf /var/lib/apt/lists/* ; \
    :

ADD https://github.com/krallin/tini/releases/download/v0.18.0/tini /usr/local/sbin/tini

RUN set -ex; \
    sed -i "/fr_FR.*UTF-8/s/^# //" /etc/locale.gen ; \
    locale-gen ; \
    useradd --home-dir /strass --create-home --system strass ; \
    chmod +x /usr/local/sbin/tini ; \
    :

# Persister les sessions PHP.
VOLUME /var/lib/php/sessions

WORKDIR /strass
