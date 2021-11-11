FROM ubuntu:18.04 as builder

RUN apt-get update && apt-get upgrade -y && apt-get install -y uuid-dev libexpat1-dev libsqlite3-dev libmysqlclient-dev \
libmagic-dev libexif-dev libcurl4-openssl-dev \
libavutil-dev libavcodec-dev libavformat-dev libavdevice-dev \
libavfilter-dev libavresample-dev libswscale-dev libswresample-dev libpostproc-dev \
cmake git g++ wget autoconf build-essential libtool libffmpegthumbnailer-dev \
pkg-config

ARG VERSION
ENV VERSION ${VERSION:-1.3.1}

WORKDIR /tmp

RUN wget https://github.com/gerbera/gerbera/archive/v${VERSION}.tar.gz && tar -xzvf v${VERSION}.tar.gz

RUN sh gerbera-${VERSION}/scripts/install-pupnp18.sh
RUN sh gerbera-${VERSION}/scripts/install-taglib111.sh
RUN sh gerbera-${VERSION}/scripts/install-duktape.sh

RUN apt-get install -y libmatroska-dev
RUN mkdir build && cd build && cmake ../gerbera-${VERSION} -DWITH_MAGIC=1 -DWITH_CURL=1 -DWITH_JS=1 \
-DWITH_TAGLIB=1 -DWITH_AVCODEC=1 -DWITH_FFMPEGTHUMBNAILER=1 -DWITH_EXIF=1 -DWITH_SYSTEMD=0 && make -j4 && make install




FROM ubuntu:18.04

RUN apt-get update && apt-get upgrade -y && apt-get install -y libixml10 \
    libexpat1 libsqlite3-0 libcurl4 libmagic1 libavformat57 \
    libffmpegthumbnailer4v5 libmatroska6v5 libexif12

ARG VERSION
ENV VERSION ${VERSION:-1.3.1}

copy --from=builder /usr/local/bin/gerbera /usr/local/bin/gerbera
copy --from=builder /usr/local/share/gerbera /usr/local/share/gerbera

copy --from=builder /usr/local/lib/libduktape* /usr/local/lib/
copy --from=builder /usr/local/include/duktape.h /usr/local/include/
copy --from=builder /usr/local/include/duk_config.h /usr/local/include/

copy --from=builder /usr/local/bin/taglib-config /usr/local/bin/
copy --from=builder /usr/local/lib/pkgconfig/taglib.pc /usr/local/lib/pkgconfig/taglib.pc
copy --from=builder /usr/local/lib/libtag.a /usr/local/lib/libtag.a
copy --from=builder /usr/local/include/taglib /usr/local/include/taglib
copy --from=builder /usr/local/lib/libtag_c.a /usr/local/lib/libtag_c.a
copy --from=builder /usr/local/include/taglib/tag_c.h /usr/local/include/taglib/tag_c.h
copy --from=builder /usr/local/lib/pkgconfig/taglib_c.pc /usr/local/lib/pkgconfig/taglib_c.pc

copy --from=builder /usr/local/lib/libupnp* /usr/local/lib/

RUN useradd gerbera 

RUN rm -rf /tmp/* && \
    mkdir -p /media/pictures /media/videos /media/music /home/gerbera && \
    chown gerbera:gerbera /home/gerbera 

USER gerbera

RUN mkdir -p /home/gerbera/.config/gerbera 

VOLUME [ "/media/pictures", "/media/videos", "/media/music", "/home/gerbera/.config/gerbera" ]

LABEL GERBERA-VERSION=${VERSION}

ENV LD_LIBRARY_PATH=/usr/local/lib

ENTRYPOINT [ "/usr/local/bin/gerbera" ]
