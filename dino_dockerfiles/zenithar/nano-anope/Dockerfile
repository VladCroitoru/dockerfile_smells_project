FROM frolvlad/alpine-glibc:latest
MAINTAINER Thibault NORMAND <me@zenithar.org>

WORKDIR /src

RUN apk add --update -t build-deps make cmake gcc g++ git wget bison openssl-dev \
    && apk add -u musl && rm -rf /var/cache/apk/* \
    && wget https://github.com/anope/anope/releases/download/2.0.5/anope-2.0.5-source.tar.gz \
    && tar zxvf anope-2.0.5-source.tar.gz \
    && cd /src/anope-2.0.5-source \
    && mkdir build \
    && cd build \
    && cmake \
        -DINSTDIR:STRING=/opt/services \
        -DDEFUMASK:STRING=077  \
        -DCMAKE_BUILD_TYPE:STRING=RELEASE \
        -DUSE_RUN_CC_PL:BOOLEAN=ON \
        -DUSE_PCH:BOOLEAN=ON .. \
    && make \
    && make install \
    && addgroup anope \
    && adduser -G anope -D anope \
    && chown -R anope:anope /opt/services \
    && rm -Rf /src \
    && apk del --purge build-deps \
    && apk add --update libstdc++ \
    && rm -rf /var/cache/apk/*

ADD run.sh /tmp/run.sh

WORKDIR /opt/services
EXPOSE 80
CMD ["/tmp/run.sh"]
