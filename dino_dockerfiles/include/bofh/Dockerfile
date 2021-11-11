FROM ubuntu:14.04
MAINTAINER include <francisco.cabrita@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

RUN apt-get update && apt-get -yq upgrade && \
    apt-get -yq install language-pack-en && \
    locale-gen en_US.UTF-8 && \
    dpkg-reconfigure locales && \
    apt-get -yq install \
    build-essential \
    software-properties-common \
    gcc make automake autoconf \
    curl wget && \
    echo "--- python ---" && \
    apt-get -yq install \
    python-dev \
    python-software-properties \
    python-simplejson && \
    curl -O https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    pip install \
    boto \
    awscli \
    paramiko \
    PyYAML \
    Jinja2 \
    httplib2 && \
    apt-get -yq install \
    flex \
    gawk \
    nmap \
    snmp \
    whois \
    bison \
    s3cmd \
    unzip \
    fping \
    pwgen \
    openssl \
    gettext \
    pngcrush \
    imagemagick \
    ncurses-dev \
    binutils-doc \
    zlib1g \
    libtool \
    libxml2 \
    libc6-dev \
    libpq-dev \
    libssl-dev \
    libffi-dev \
    zlib1g-dev \
    libyaml-dev \
    libgdbm-dev \
    libxml2-dev \
    libxslt-dev \
    libxslt1-dev \
    libgnutls-dev \
    libexpat1-dev \
    libghc-zlib-dev \
    libreadline6-dev \
    libmagickwand-dev \
    libcurl4-gnutls-dev \
    git \
    zip \
    mtr \
    ntp \
    lsof \
    htop \
    tmux \
    dstat \
    socat \
    iotop \
    rsync \
    telnet \
    rlwrap \
    ntpdate \
    sysstat \
    vim-tiny \
    traceroute \
    libsqlite3-dev \
    sqlite3 \
    postgresql-client \
    nodejs \
    nodejs-dev \
    npm && \
    echo "--- redis ---" && \
    apt-add-repository -y ppa:rwky/redis && \
    apt-get update -y && \
    apt-get -yq install redis-tools && \
    echo "--- cleanup ---" && \
    apt-get -yq autoremove && \
    apt-get -y clean && \
    rm -rf /var/lib/lists/*
