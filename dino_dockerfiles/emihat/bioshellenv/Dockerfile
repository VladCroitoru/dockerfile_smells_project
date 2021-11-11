FROM alpine:3.2

MAINTAINER emihat <emi.2sheds.hattori@gmail.com>

ENV SAMTOOLS_VERSION 1.3.1
ENV TABIX_VERSION 0.2.6

RUN apk add --update pcre-dev openssl-dev curl jq git bash coreutils util-linux \
 && apk add --virtual build-dependencies build-base \
 && curl -L -o samtools-${SAMTOOLS_VERSION}.tar.bz2 \
    http://jaist.dl.sourceforge.net/project/samtools/samtools/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2 \
 && tar jxvf samtools-${SAMTOOLS_VERSION}.tar.bz2  \
 && cd samtools-${SAMTOOLS_VERSION}/ \
 && ./configure --without-curses \
 && make \
 && make install \
 && curl -L -o tabix-${TABIX_VERSION}.tar.bz2 \
    http://downloads.sourceforge.net/project/samtools/tabix/tabix-${TABIX_VERSION}.tar.bz2 \
 && tar jxvf tabix-${TABIX_VERSION}.tar.bz2  \
 && cd tabix-${TABIX_VERSION}/ \
 && make \
 && ln -sf /tabix-${TABIX_VERSION}/tabix /usr/local/bin/ \
 && apk del build-dependencies \
 && rm -rf /var/chache/apk/* \
 && mkdir /data \
 && cd /data \
 && git clone https://github.com/bio-shell/study1.git

WORKDIR /data/study1/data

CMD ["bash"]
