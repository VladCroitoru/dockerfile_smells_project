FROM centos:7

ENV BOOST_INSTALL_VERSION=1.60.0 \
    MAPNIK_INSTALL_VERSION=3.0.21 \
    PATH=/usr/pgsql-11/bin:$PATH \
    CC=/usr/bin/clang \
    CXX=/usr/bin/clang++ \
    LD_LIBRARY_PATH=/usr/local/lib

RUN yum -y update && \
    yum -y install epel-release && \
    yum -y install https://download.postgresql.org/pub/repos/yum/11/redhat/rhel-7-x86_64/pgdg-centos11-11-2.noarch.rpm && \
    yum -y install \
        bzip2 \
        bzip2-devel \
        cairo-devel \
        clang \
        file \
        gcc-c++ \
        gdal-devel \
        git \
        harfbuzz-devel \
        libjpeg-turbo-devel \
        libtiff-devel \
        libwebp-devel \
        make \
        postgresql11-devel \
        postgis2_11-devel \
        proj-devel \
        proj-epsg \
        python-devel \
        sqlite-devel \
        tar \
        wget \
        which \
    && \
    yum clean all && \
    # Install required Boost components
    cd /opt && \
    export BOOST_DOWNLOAD_VERSION=$(echo $BOOST_INSTALL_VERSION | tr . _) && \
    wget -nv http://downloads.sourceforge.net/project/boost/boost/${BOOST_INSTALL_VERSION}/boost_${BOOST_DOWNLOAD_VERSION}.tar.bz2 && \
    export BOOST_DOWNLOAD_VERSION=$(echo $BOOST_INSTALL_VERSION | tr . _) && \
    tar -xjf boost_${BOOST_DOWNLOAD_VERSION}.tar.bz2 && \
    cd /opt/boost_${BOOST_DOWNLOAD_VERSION} && \
    ./bootstrap.sh --with-toolset=clang && \
    ./b2 -d0 --with-thread --with-thread --with-filesystem --with-python --with-regex -sHAVE_ICU=1 --with-program_options --with-system toolset=clang release install && \
    # Install Mapnik
    cd /opt && \
    git clone -b v${MAPNIK_INSTALL_VERSION} --single-branch --recursive https://github.com/mapnik/mapnik.git mapnik-${MAPNIK_INSTALL_VERSION} && \
    cd /opt/mapnik-${MAPNIK_INSTALL_VERSION} && \
    ./configure CXX=clang++ CC=clang && \
    make --silent && \
    make install && \
    # Cleanup source downloads and install working folders
    rm -rf /opt/boost* && \
    rm -rf /opt/mapnik*
