FROM srid/mint-exporter

# Building sqlite manually because the base image (Debian) has an
# outdated version, 3.7, that doesn't import from .csv correctly.
ENV SQLITE_URL http://www.sqlite.org/2014/sqlite-autoconf-3080702.tar.gz
RUN cd /tmp && \
    curl ${SQLITE_URL} > sqlite.tgz && \
    tar zxf sqlite.tgz && \
    cd sqlite-autoconf* && \
    ./configure --disable-dynamic-extensions --enable-static --disable-shared && \
    make all install && \
    cd - && \
    rm -rf sqlite*

ADD mint2db.sh /usr/bin/mint2db.sh

CMD ["mint2db.sh"]
