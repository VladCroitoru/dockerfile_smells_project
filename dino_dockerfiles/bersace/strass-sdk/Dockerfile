#
# Outils de construction de style et des données SQLite de strass
#

FROM bersace/strass-runtime

RUN set -ex; \
    apt-get update -y; \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        build-essential \
        faketime \
        git \
        make \
        openssh-client \
        python3-dev \
        python3-pip \
        sqlite3 \
       ; \
    apt-get clean; \
    rm -rf /var/lib/apt/lists/*; \
    :

RUN set -ex; \
    ln -s php /usr/lib/php ; \
    curl -Lo /usr/local/bin/phpunit https://phar.phpunit.de/phpunit-5.phar ; \
    chmod +x /usr/local/bin/phpunit ; \
    phpunit --version ; \
    :

RUN set -ex; \
    /usr/bin/pip3 install --upgrade pip setuptools wheel; \
    /usr/local/bin/pip3 install --no-cache-dir --upgrade libsass pytest pyyaml selenium six webassets; \
    /usr/local/bin/pip3 check; \
    rm -rf ~/.cache/; \
    :
