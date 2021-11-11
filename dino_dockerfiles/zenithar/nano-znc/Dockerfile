FROM frolvlad/alpine-glibc:latest
MAINTAINER Thibault NORMAND <me@zenithar.org>

WORKDIR /src

RUN apk add --update -t build-deps make gcc g++ git wget bison openssl-dev swig perl-dev python3-dev icu-dev \
    && apk add -u musl && rm -rf /var/cache/apk/* \
    && wget http://znc.in/releases/znc-1.6.5.tar.gz \
    && tar zxvf znc-1.6.5.tar.gz \
    && cd /src/znc-1.6.5 \
    && ./configure --prefix="/opt/znc" --enable-python --enable-perl \
    && make \
    && make install \
    && rm -Rf /src && apk del --purge build-deps \
    && apk add --update libstdc++ icu \
    && addgroup znc \
    && mkdir /data \
    && adduser -G znc -D -h /data znc \
    && chown -R znc:znc /opt/znc \
    && chown -R znc:znc /data

USER znc
WORKDIR /opt/znc

VOLUME /data

EXPOSE 6697
ENTRYPOINT ["/opt/znc/bin/znc"]
CMD [""]

