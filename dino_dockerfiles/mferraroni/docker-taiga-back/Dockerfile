FROM python:3-slim

MAINTAINER Maik Hummel <m@ikhummel.com>

ENV TAIGA_VERSION 3.1.0

WORKDIR /opt/

RUN buildDeps='build-essential binutils-doc autoconf flex bison libjpeg-dev libfreetype6-dev zlib1g-dev libgdbm-dev libncurses5-dev automake libtool libffi-dev curl git libpq-dev'; \
    set -x && \
    apt-get -qq update && \
    apt-get -qq install -y $buildDeps && \
    apt-get -qq install -y netcat gettext moreutils libpq5 libxslt1-dev libxml2-dev libjpeg62 libzmq3-dev --no-install-recommends && \
    apt-mark manual libxslt1-dev && \
    
    pip install circus==0.13 && \
    
    useradd -d `pwd` taiga && \
    mkdir -p media static logs taiga-back taiga && \

    curl -sL "https://api.github.com/repos/taigaio/taiga-back/tarball/${TAIGA_VERSION}" | tar xz -C taiga-back --strip-components=1 && \
    cd taiga-back && \
    pip install -r requirements.txt && \

    # clean up
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    apt-get purge -y $buildDeps && \
    apt-get autoremove -y && \
    apt-get clean

COPY circus.ini conf.env start ./

COPY dockerenv.py taiga-back/settings/dockerenv.py

VOLUME /usr/local/taiga/media /usr/local/taiga/static /usr/local/taiga/logs

EXPOSE 8000

CMD ./start
