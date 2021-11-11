FROM golang:alpine

#Add in libpostal
ENV LIBPOSTAL_DATA=/data

#Add in libpostal
RUN apk add --no-cache snappy curl bash findutils tar coreutils \
 && apk add --no-cache --virtual .build-deps snappy-dev git autoconf automake make gcc libtool libc-dev \
 && mkdir -p /tmp/src \
 && cd /tmp/src \
 && git clone https://github.com/openvenues/libpostal.git \
 && cd libpostal \
 && echo "ACLOCAL_AMFLAGS = -I m4" >> Makefile.am \
 && echo "AC_CONFIG_MACRO_DIR([m4])" >> configure.ac \
 && mkdir -p m4 \
 && sed -i -e 's/\(\s*.*\/libpostal_data\s*download\s*all\s*\$(datadir)\/libpostal\)/#\1/g' src/Makefile.am \
 && ./bootstrap.sh \
 && ./configure --prefix=/usr --datadir=/data \
 && make -j \
 && make install \
 && cd / \
 && /usr/bin/libpostal_data download all $LIBPOSTAL_DATA/libpostal \
 && apk del .build-deps \
 && rm -fr .build-deps /tmp/src /root/.ash_history

RUN apk add --no-cache git gcc pkgconfig snappy-dev autoconf automake make libtool libc-dev

COPY ./docker-entrypoint.sh /
RUN chmod a+x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
