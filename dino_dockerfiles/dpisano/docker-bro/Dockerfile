# Bro Sandbox - Bro 2.5.3
#
FROM alpine:3.8

# Metadata
LABEL program=bro

# Specify container username e.g. training, demo
ENV VIRTUSER bro
# Specify program
ENV PROG bro
# Specify source extension
ENV EXT tar.gz
# Specify Bro version to download and install (e.g. bro-2.3.1, bro-2.4)
ENV VERS 2.5.5
# Install directory
ENV PREFIX /opt/bro
# Path should include prefix
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PREFIX/bin

COPY patches /tmp

RUN apk add --no-cache zlib openssl libstdc++ libpcap geoip libgcc bash supervisor python
RUN apk add --no-cache -t .build-deps \
                          linux-headers \
                          openssl-dev \
                          libpcap-dev \
                          python-dev \
                          geoip-dev \
                          zlib-dev \
                          binutils \
                          fts-dev \
                          cmake \
                          clang \
                          bison \
                          perl \
                          make \
                          flex \
                          git \
                          g++ \
                          fts \
                          swig && \
    cd /tmp && \
    wget https://www.bro.org/downloads/$PROG-$VERS.$EXT && \
    tar -xzf $PROG-$VERS.$EXT && \
    rm -rf ./$PROG-$VERS.$EXT && \
    cd $PROG-$VERS && \
    patch -p1 < /tmp/bro-musl.patch && \
    cp /tmp/FindFTS.cmake cmake && \
    cd aux/binpac && \
    patch -p1 < /tmp/binpac-musl.patch && \
    cd ../../ && \
    CC=clang ./configure --prefix=$PREFIX && \
    make && \
    make install && \
    cd .. \
    rm -rf $PROG-$VERS && \
    chmod u+s $PREFIX/bin/$PROG ; \
    chmod u+s $PREFIX/bin/broctl ; \
    chmod u+s $PREFIX/bin/capstats ; \
    strip -s $PREFIX/bin/bro && \
    rm -rf /var/cache/apk/* && \
    rm -rf /tmp/* && \
    apk del --purge .build-deps

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

VOLUME  /opt/bro/logs /opt/bro/spool /opt/bro/etc
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/conf.d/supervisord.conf"]
