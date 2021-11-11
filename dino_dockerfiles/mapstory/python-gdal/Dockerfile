FROM python:2.7.15-jessie
MAINTAINER Tyler Battle <tbattle@boundlessgeo.com>

ENV TMP /tmp
ENV GDAL_VERSION 2.2.2

WORKDIR $TMP

### Build and install GDAL
RUN set -ex \
    && wget -qP $TMP http://download.osgeo.org/gdal/$GDAL_VERSION/gdal-$GDAL_VERSION.tar.gz \
    && tar -xf $TMP/gdal-$GDAL_VERSION.tar.gz -C $TMP \

    && wget -qP $TMP http://s3.amazonaws.com/etc-data.koordinates.com/gdal-travisci/install-libkml-r864-64bit.tar.gz \
    && tar -xzf $TMP/install-libkml-r864-64bit.tar.gz -C $TMP \


    && cp -r $TMP/install-libkml/include/* /usr/local/include \
    && cp -r $TMP/install-libkml/lib/* /usr/local/lib \

    && cd $TMP/gdal-$GDAL_VERSION \
    && ./configure --with-python --with-libkml \
    && make \
    && make install \
    && ldconfig \
    && cd .. \
    && rm -r gdal* \
    && pip install --no-cache-dir GDAL==$GDAL_VERSION
