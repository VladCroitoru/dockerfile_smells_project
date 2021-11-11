FROM centos
MAINTAINER Frezbo <docker@frezbo.com>
#tracking
ENV DATE 2017-03-31
ENV OPENSSL_VERSION="1.0.2h"
#from https://github.com/openssl/openssl/pull/872/files
COPY no-des.patch /opt
RUN yum -y update \
### Install tool for compiling
&& yum -y install gcc \
&& yum -y install make \
&& yum -y install wget \
&& yum -y install tar \
&& yum -y install perl \
&& yum -y install git \
&& yum -y install patch \
&& yum clean all 
## BUILD OpenSSL
RUN wget "https://www.openssl.org/source/openssl-${OPENSSL_VERSION}.tar.gz" -P /opt/ \
&& cd /opt/ \
&& tar xzf openssl-${OPENSSL_VERSION}.tar.gz \
&& rm -f openssl-${OPENSSL_VERSION}.tar.gz \
&& git clone https://github.com/cloudflare/sslconfig.git \
&& cd openssl-${OPENSSL_VERSION} \
&& patch -p1 < ../sslconfig/patches/openssl__chacha20_poly1305_draft_and_rfc_ossl102g.patch \
&& mv /opt/no-des.patch /opt/openssl-${OPENSSL_VERSION} \
&& patch -p1 crypto/cms/cms_kari.c < no-des.patch
RUN cd /opt/openssl-${OPENSSL_VERSION} \
&& ./config --prefix=/usr no-ssl3 no-rc4 no-camellia no-seed no-comp no-srp no-psk no-idea no-des no-descbcm no-dh \
&& make depend \
&& make \
#&& make test \ #make test fails when des is disabled
&& make install \
&& rm -rf /opt/openssl-${OPENSSL_VERSION} /opt/sslconfig
