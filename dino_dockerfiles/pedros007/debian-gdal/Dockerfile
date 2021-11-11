FROM python:2
MAINTAINER Peter Schmitt "pschmitt@gmail.com"

# To build from GitHub, comment out curl http://download.osgeo... and
# cd, replace with something like:
#
#    curl -L https://github.com/OSGeo/gdal/archive/2c866d3c62bb52852d7ab6850b63d3a3d81b51a1.tar.gz | tar zxv -C /tmp && \
#    cd /tmp/gdal-2c866d3c62bb52852d7ab6850b63d3a3d81b51a1/gdal && \
#
# Then build:
#   docker build -t pedros007/debian-gdal:2c866d3 .

# To build from a release:
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y \
    build-essential make cmake curl ca-certificates libcurl4-gnutls-dev \
    libjasper1 libjasper-dev \
    shapelib libproj-dev libproj0 proj-data libgeos-3.4.2 libgeos-c1 libgeos-dev \
    postgresql-client-common libpq-dev \
    -y --no-install-recommends && \
    git clone -b master https://github.com/uclouvain/openjpeg.git /tmp/openjpeg && \
    mkdir /tmp/openjpeg/build && cd /tmp/openjpeg/build && cmake .. -DCMAKE_INSTALL_PREFIX=/usr && make && make install && \
    pip install numpy && \
    curl http://download.osgeo.org/gdal/2.3.2/gdal-2.3.2.tar.gz | tar zxv -C /tmp && \
    cd /tmp/gdal-2.3.2 && \
    ./configure \
    --prefix=/usr \
    --with-threads \
    --with-hide-internal-symbols=yes \
    --with-rename-internal-libtiff-symbols=yes \
    --with-rename-internal-libgeotiff-symbols=yes \
    --with-libtiff=internal \
    --with-geotiff=internal \
    --with-geos \
    --with-pg \
    --with-curl \
    --with-static-proj4=yes \
    --with-openjpeg=yes \
    --with-ecw=no \
    --with-grass=no \
    --with-hdf5=no \
    --with-java=no \
    --with-mrsid=no \
    --with-perl=no \
    --with-python=yes \
    --with-webp=no \
    --with-xerces=no && \
    make -j $(grep --count ^processor /proc/cpuinfo) && \
    make install && \
    apt-get remove --purge -y libcurl4-gnutls-dev libproj-dev libgeos-dev libpq-dev && \
    rm -rf /var/lib/apt/lists/* /tmp/*

# Set HOME dir so AWS credentials can be fetched at ~/.aws/credentials
# https://lists.osgeo.org/pipermail/gdal-dev/2017-July/046846.html
# I had issues with Python bindings unless I set PYTHONPATH accordingly.
ENV HOME=/root \
    PYTHONPATH=/usr/lib/python2.7/site-packages
