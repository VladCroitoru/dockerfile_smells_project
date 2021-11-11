FROM python:3.5-alpine

VOLUME /in
VOLUME /out

WORKDIR /code

RUN apk --update add \
    ca-certificates \
    gdal \
    geos \
    openssl \
    tini \
    --update-cache \
    --repository http://dl-3.alpinelinux.org/alpine/edge/community/ --allow-untrusted \
    --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted

RUN apk --update add --virtual build-dependencies \
        build-base \
        gdal-dev \
        geos-dev \
        --update-cache \
        --repository http://dl-3.alpinelinux.org/alpine/edge/community/ --allow-untrusted \
        --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted \
    && ln -s /usr/include/locale.h /usr/include/xlocale.h \
    && pip install \
        numpy \
    && pip install \
        fiona \
        rasterio \
        shapely \
    && apk del build-dependencies

COPY ./disaggregate_viewsheds.py /code

ENV VIEWSHEDS_PER_FILE=32
ENV OVERFLOW=31

WORKDIR /code
ENTRYPOINT ["sbin/tini", "--"]
CMD ["/usr/bin/python", "disaggregate_viewsheds.py"]
