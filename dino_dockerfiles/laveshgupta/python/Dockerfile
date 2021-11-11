FROM ubuntu:14.04.2

RUN \
    cd / && \
    apt-get update && \
    apt-get purge -y python.* && \
    apt-get install -y --no-install-recommends autotools-dev blt-dev bzip2 dpkg-dev gcc-multilib g++-multilib libbluetooth-dev libbz2-dev libexpat1-dev libffi-dev libffi6 libffi6-dbg libgdbm-dev  libgpm2 libncursesw5-dev libreadline-dev libsqlite3-dev libssl-dev libssl-dev libtinfo-dev  mime-support netbase net-tools python-crypto python-mox3 python-pil python-ply quilt tk-dev zlib1g-dev && \
    apt-get install -y --no-install-recommends autoconf automake bzr bzip2 ca-certificates curl file g++ gcc git imagemagick libbz2-dev libc6-dev libcurl4-openssl-dev libevent-dev libffi-dev libglib2.0-dev libjpeg-dev liblzma-dev libmagickcore-dev libmagickwand-dev libmysqlclient-dev libncurses-dev libpq-dev libreadline-dev libsqlite3-dev libssl-dev libtool libwebp-dev libxml2-dev libxslt-dev libyaml-dev make mercurial openssh-client patch subversion wget xz-utils zlib1g-dev && \
    mkdir -p /usr/src/python && \
    curl -SL "https://www.python.org/ftp/python/2.7.9/Python-2.7.9.tgz" -o python.tgz && \
    tar -xzC /usr/src/python --strip-components=1 -f python.tgz && \
    rm python.tgz && \
    cd /usr/src/python && \
    apt-get update && \
    ./configure --enable-shared --enable-unicode=ucs4 --enable-ipv6 && \
    make -j$(nproc) && \
    make install && \
    ldconfig && \
    curl -SL 'https://bootstrap.pypa.io/get-pip.py' | python2 && \
    find /usr/local \( -type d -a -name test -o -name tests \) -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) -exec rm -rf '{}' + && \
    cd / && \
    rm -rf /usr/src/python && \
    pip install cherrypy && \
    pip install pyyaml && \
    apt-get update

CMD ["python2"]
    
    