FROM ubuntu:focal
MAINTAINER danielpops@gmail.com

RUN apt-get update > /dev/null \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        bison \
        cmake \
        curl \
        doxygen \
        g++ \
        gcc \
        git-core \
        gnutls-bin \
        graphviz \
        libical-dev \
        libldap2-dev \
        libgcrypt20-dev \
        libglib2.0-dev \
        libgpgme-dev \
        libhiredis-dev \
        libksba-dev \
        libmicrohttpd-dev \
        libpcap-dev \
        libpq-dev \
        libsnmp-dev \
        libssh-gcrypt-dev \
        libxml2-dev \
        make \
        nmap \
        nodejs \
        pkg-config \
        postgresql \
        postgresql-contrib \
        postgresql-server-dev-all \
        redis-server \
        rsync \
        sudo \
        uuid-dev \
        vim \
        xml-twig-tools \
        xmltoman \
        xsltproc \
        yarnpkg

# yarn for some reason is installed as yarnpkg and not yarn
RUN ln -s /usr/bin/yarnpkg /usr/bin/yarn

WORKDIR /openvas
RUN for i in gvm-libs gvmd openvas gsa; do \
        git clone --depth=1 --branch v20.8.0 https://github.com/greenbone/$i; \
        cd $i; \
        cmake .; \
        make install; \
        cd ..; \
        rm -rf $i; \
        ldconfig; \
    done


RUN echo 'nobody ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/01-nobody && \
        chown -R nobody /openvas && \
        chown -R nobody /usr/local/var/
ADD redis.conf /etc/redis/redis.conf
ADD setup.sh /openvas/setup.sh
USER nobody

