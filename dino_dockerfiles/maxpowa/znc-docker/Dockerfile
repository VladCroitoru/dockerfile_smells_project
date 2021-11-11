FROM alpine:3.3

ENV ZNC_VERSION 1.6.3
ENV ZNCSTRAP_BRANCH dev

RUN apk add --no-cache --update -t build-deps make wget bison && \
    apk add --no-cache -u musl gcc g++ icu-dev openssl-dev swig perl-dev python3-dev && \
    rm -rf /var/cache/apk/* && \
    mkdir -p /src && \
    cd /src && \
    wget http://znc.in/releases/znc-${ZNC_VERSION}.tar.gz && \
    tar zxvf znc-${ZNC_VERSION}.tar.gz && \
    cd /src/znc-${ZNC_VERSION} && \
    ./configure --prefix="/opt/znc" --enable-python --enable-perl && \
    make && \
    make install && \
    rm -Rf /src && apk del --purge build-deps && \
    apk add --no-cache --update libstdc++ icu sudo bash git

RUN git clone -b ${ZNCSTRAP_BRANCH} https://github.com/ProjectFirrre/zncstrap/ /zncstrap && \
    rm -Rf /opt/znc/share/znc/webskins && \
    rm -Rf /opt/znc/share/znc/modules && \
    mv /zncstrap/webskins /opt/znc/share/znc/ && \
    mv /zncstrap/modules /opt/znc/share/znc/

RUN adduser -D znc && \
    chown -R znc:znc /opt/znc
ADD docker-entrypoint.sh /entrypoint.sh
ADD znc.conf.default /znc.conf.default
ADD identserv.cpp /identserv.cpp
RUN chmod +x /entrypoint.sh
RUN chmod 644 /znc.conf.default
RUN chmod 644 /identserv.cpp

VOLUME /znc-data

# 11300 is our identserver, map it to 113 on the host
EXPOSE 6667 11300
ENTRYPOINT ["/entrypoint.sh"]
CMD [""]
