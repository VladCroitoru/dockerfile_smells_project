FROM centos
MAINTAINER architect.bian
LABEL name="centos7" license="GPLv2" build-date="20161023"

ENV OPENSSL_VERSION OpenSSL_1_1_0b

RUN yum update -y && yum install -y epel-release && yum install -y  gcc gcc-c++ perl automake autoconf libtool make yum-plugin-priorities && yum update -y && yum install -y  wget net-tools && mkdir -p /data/softs && mkdir -p /data/env && mkdir -p /data/web && cd /data/softs && wget "http://zlib.net/zlib-1.2.8.tar.gz" && tar -zxf zlib-1.2.8.tar.gz && cd zlib-1.2.8 && ./configure && make && make install && rm -rf /data/softs/zlib-1.2.8* && cd /data/softs && yum remove openssl -y && wget  "https://codeload.github.com/openssl/openssl/tar.gz/$OPENSSL_VERSION" && tar -zxf $OPENSSL_VERSION && cd openssl-$OPENSSL_VERSION && ./config --prefix=/usr/ --openssldir=/etc/ssl shared zlib && make && make install && rm -rf /data/softs/OpenSSL* /data/softs/openssl*

CMD ["/bin/bash"]





