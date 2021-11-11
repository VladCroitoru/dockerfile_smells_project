FROM alpine:3.6

MAINTAINER Brian Winkers <bwinkers@gmail.com>

ARG HITCH_VERSION=1.4.6
ARG HITCH_CHECKSUM=b095e465f0fc37c5e46cfc0fbcf987ba90ed660caf7f559547df8dea985fec2b

ENV HITCH_USER nobody
ENV HITCH_GROUP nogroup
ENV HITCH_CONFIG /etc/hitch/hitch.conf
ENV HITCH_WORKERS 1

RUN echo "http://dl-3.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories && \
apk add --update --no-cache gcc

RUN apk add --no-cache openssl libev

RUN apk add --no-cache --virtual .build-deps curl libev-dev openssl-dev autoconf libtool py-docutils make automake pkgconfig gcc musl-dev byacc flex \
    && mkdir /usr/src \
    && cd /usr/src \
    && curl -SL -o hitch.tar.gz https://hitch-tls.org/source/hitch-${HITCH_VERSION}.tar.gz \
    && echo "${HITCH_CHECKSUM}  hitch.tar.gz" > sha256sums.txt \
    && sha256sum -c sha256sums.txt \
    && tar xzf hitch.tar.gz \
    && cd hitch-${HITCH_VERSION} \
    && ./configure --bindir=/usr/bin --sbindir=/usr/sbin --libexecdir=/usr/libexec --sysconfdir=/etc --localstatedir=/var --libdir=/usr/lib \
    && make \
    && make install \
    && cd /usr/src \
    && rm hitch.tar.gz sha256sums.txt \
    && apk del .build-deps

RUN mkdir /etc/hitch

COPY hitch.conf /etc/hitch/hitch.conf

ADD run.sh /usr/sbin/run.sh

RUN chmod +x /usr/sbin/run.sh

EXPOSE 443

CMD ["run.sh"]
