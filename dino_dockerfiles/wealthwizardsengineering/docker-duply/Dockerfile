FROM debian:jessie

MAINTAINER Richard Marshall

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    gcc \
    ncftp \
    pwgen \
    python-boto \
    python-lockfile \
    python-paramiko \
    python-pycryptopp \
    lftp \
    python-dev \
    python-setuptools \
    librsync-dev \
    curl \
    awscli \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/* \
    && cd /tmp \
    && curl -L https://launchpad.net/duplicity/0.7-series/0.7.05/+download/duplicity-0.7.05.tar.gz \
    | tar -xz \
    && cd duplicity-0.7.05 \
    && python setup.py install \
    && curl -L http://downloads.sourceforge.net/project/ftplicity/duply%20%28simple%20duplicity%29/1.10.x/duply_1.10.1.tgz \
    | tar -xz \
    && mv duply_1.10.1/duply /usr/bin/duply

ENV HOME /root
ENV SOURCE /source

ENV KEY_TYPE      RSA
ENV KEY_LENGTH    2048
ENV SUBKEY_TYPE   RSA
ENV SUBKEY_LENGTH 2048
ENV NAME_REAL     Duply Backup
ENV NAME_EMAIL    duply@localhost
ENV PASSPHRASE    random

VOLUME ["/root"]

COPY files/entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
