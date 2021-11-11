FROM rocker/geospatial:latest
MAINTAINER "Noam Ross" ross@ecohealthalliance.org

## Install GRASS and plugins

RUN apt-get update \
## needed to not prompt for mysql DB password
&&    export DEBIAN_FRONTEND=noninteractive \
## no-upgrade skips things already installed
&&    apt-get install -y --no-install-recommends --no-upgrade \
      cmake libboost-all-dev flex bison debhelper dpatch autoconf2.13 \
      autotools-dev python-dev g++ gcc gettext graphviz libcairo2-dev libfftw3-dev \
      libfreetype6-dev libgdal1h libgdal1-dev libglu1-mesa-dev libglw1-mesa-dev \
      libncurses5-dev libproj-dev libreadline-dev libsqlite3-dev libtiff5-dev \
      libwxgtk3.0-dev libxmu-dev libxmu-headers libxt-dev mesa-common-dev \
      proj-bin proj-data python-numpy python-wxgtk3.0 subversion wx-common zlib1g-dev \
      netcdf-bin libnetcdf-dev libgegl-dev  doxygen python-sphinx \
      postgresql libgeotiff-dev libblas-dev mysql-server \
      libatlas-dev libblas-dev liblapack3gf liblapack-dev \
      opencl-headers ocl-icd-libopencl1 liblas-bin liblas-c-dev python-gdal \
&& wget https://grass.osgeo.org/grass72/source/grass-7.2.0.tar.gz \
&& tar xzfv grass-7.2.0.tar.gz \
&& cd grass-7.2.0 \
&& CFLAGS="-g -Wall -Werror-implicit-function-declaration -fno-common -Wextra -Wunused" \
      CXXFLAGS="-g -Wall"  \
      ./configure \
         --prefix=/usr/local \
         --with-gdal --with-proj --with-proj-share=/usr/share \
         --with-glw --with-nls --with-readline \
         --with-cxx --enable-largefile \
         --with-freetype --with-freetype-includes=/usr/include/freetype2 \
         --with-sqlite --with-cairo --with-python=/usr/bin/python-config \
         --with-wxwidgets --with-geos \
         --with-blas --with-blas-includes=/usr/include/atlas/ \
         --with-lapack --with-lapack-includes=/usr/include/atlas/ \
         --with-netcdf=/usr/bin/nc-config --with-odbc=yes \
         --with-openmp=yes --with-pthread=no --with-postgres=yes \
         --with-postgres-includes=/usr/include/postgresql \
         --with-postgres-libs=/usr/lib/postgresql \
         --with-mysql=yes --with-mysql-includes=/usr/include/mysql \
         --with-mysql-libs=/usr/lib/mysql \
&& make -j2 \
&& make install \
&& cd .. \
&& rm -r grass-7.2.0 \
&& rm grass-7.2.0.tar.gz \
&& apt-get clean \

## Install grass7 R package
  && install2.r --error \
    --repos 'https://cloud.r-project.org/' \
    rgrass7
