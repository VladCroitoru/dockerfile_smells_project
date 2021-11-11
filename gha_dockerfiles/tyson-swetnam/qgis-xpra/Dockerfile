FROM tswetnam/xpra:bionic

USER root

# GDAL, GEOS, GRASS, QGIS, SAGA-GIS dependencies
RUN apt-get update \
    && apt-get install -y build-essential software-properties-common \
    && apt-get install -y --no-install-recommends --no-install-suggests \
        libblas-dev \
        libbz2-dev \
	libcairo2-dev \
        libcurl4-gnutls-dev \
	libexpat-dev \
        libfftw3-bin \        
        libfftw3-dev \
        libfreetype6-dev \
        libgdal-dev \
        libgeos-dev \
        libglu1-mesa-dev \
        libgsl0-dev \
        libjpeg-dev \
        libjsoncpp-dev \
        liblapack-dev \
        libncurses5-dev \
        libnetcdf-dev \
	libogdi3.2-dev \
        libopenblas-base \
        libopenblas-dev \
        libopenjp2-7 \
        libopenjp2-7-dev \
        libpdal-dev pdal \
        libpdal-plugin-python \
        libpng-dev \
        libpnglite-dev \
        libpq-dev \
        libproj-dev \
        libpython3-all-dev \
        libreadline-dev \
        libsqlite3-dev \
        libtiff-dev \
	libtiff5-dev \
        libwxgtk3.0-dev \
	libxmu-dev \	
        libzstd-dev \
        bison \
        bzip2 \  
        flex \
        g++ \
        gettext \
        gdal-bin \
        git \
	gtk2-engines-pixbuf \
	htop \
        make \
        ncurses-bin \
        netcdf-bin \
        proj-bin \
        proj-data \
        python3 \
        python3-dateutil \
        python3-dev \
        python3-magic \
        python3-numpy \
        python3-pil \
        python3-pip \
        python3-ply \
        python3-setuptools \
        python3-venv \
        sqlite3 \
        subversion \
        sudo \
	unixodbc-dev \
        wget \
	wx-common \
        xfce4-terminal \
        zlib1g-dev 

# Set gcc/g++ environmental variables for GRASS GIS compilation, without debug symbols
ENV MYCFLAGS "-O2 -std=gnu99 -m64"
ENV MYLDFLAGS "-s"
# CXX stuff:
ENV LD_LIBRARY_PATH "/usr/local/lib"
ENV LDFLAGS "$MYLDFLAGS"
ENV CFLAGS "$MYCFLAGS"
ENV CXXFLAGS "$MYCXXFLAGS"

RUN echo LANG="en_US.UTF-8" > /etc/default/locale
RUN echo en_US.UTF-8 UTF-8 >> /etc/locale.gen && locale-gen

# Configure and install GRASS
ENV GRASS_PYTHON=/usr/bin/python3

# add GRASS source repository files to the image
RUN mkdir -p /code/grass \
    && wget -nv --no-check-certificate https://grass.osgeo.org/grass76/source/grass-7.6.0.tar.gz \
    && tar xzf grass-7.6.0.tar.gz -C /code/grass --strip-components=1 \
    && rm -rf grass-7.6.0.tar.gz \
    && cd /code/grass && ./configure \
       --enable-largefile \
       --with-cxx \
       --with-nls \
       --with-readline \
       --with-sqlite \
       --with-bzlib \
       --with-zstd \
       --with-cairo --with-cairo-ldflags=-lfontconfig \
       --with-freetype --with-freetype-includes="/usr/include/freetype2/" \
       --with-fftw \
       --with-netcdf \
       --with-pdal \
       --with-proj --with-proj-share=/usr/share/proj \
       --with-geos=/usr/bin/geos-config \
       --with-postgres --with-postgres-includes="/usr/include/postgresql" \
       --with-opengl-libs=/usr/include/GL \
       --with-openmp \
       --enable-64bit \
    && make \
    && make install \
    && ldconfig
   
# Unset environmental variables to avoid later compilation issues
ENV INTEL ""
ENV MYCFLAGS ""
ENV MYLDFLAGS ""
ENV MYCXXFLAGS ""
ENV LD_LIBRARY_PATH ""
ENV LDFLAGS ""
ENV CFLAGS ""
ENV CXXFLAGS ""

# set SHELL var to avoid /bin/sh fallback in interactive GRASS GIS sessions
ENV SHELL /bin/bash
ENV LC_ALL "en_US.UTF-8"
ENV GRASS_SKIP_MAPSET_OWNER_CHECK 1

# enable simple grass command regardless of version number
RUN ln -s /usr/local/bin/grass* /usr/local/bin/grass

# install external GRASS GIS session Python API
RUN pip3 install grass-session

# add GRASS GIS envs for python usage
ENV GISBASE "/usr/local/grass/"
ENV GRASSBIN "/usr/local/bin/grass"
ENV PYTHONPATH "${PYTHONPATH}:$GISBASE/etc/python/"
ENV LD_LIBRARY_PATH "$LD_LIBRARY_PATH:$GISBASE/lib"

# once everything is built, install a couple of GRASS extensions
#RUN grass -text -c epsg:3857 ${PWD}/mytmp_wgs84 -e && \
#    echo "g.extension -s extension=r.sun.mp ; g.extension -s extension=r.sun.hourly ; g.extension -s extension=r.sun.daily" | grass -text ${PWD}/mytmp_wgs84/PERMANENT

# Compile SAGA-GIS 2.3.1  -- ltr version that works inside QGIS

ENV TZ America/Phoenix

RUN mkdir /code/saga-gis \
    && wget -nv --no-check-certificate https://ayera.dl.sourceforge.net/project/saga-gis/SAGA%20-%202/SAGA%202.3.1/saga_2.3.1_gpl2.tar.gz \
    && tar xzf saga_2.3.1_gpl2.tar.gz -C /code/saga-gis --strip-components=1 \
    && rm saga_2.3.1_gpl2.tar.gz \
    && cd /code/saga-gis \
    && ./configure \
    && make \
    && make install

# Install QGIS Latest LTR Desktop binary
RUN apt-get -y update && apt-get -f install \
    && echo "deb https://qgis.org/ubuntu bionic main" >> /etc/apt/sources.list \
    && echo "deb-src https://qgis.org/ubuntu bionic main" >> /etc/apt/sources.list \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-key 51F523511C7028C3

# Install QGIS now
RUN apt-get -y update \
    && apt-get install -y \
        python-qgis-common \
        python-qgis \
        qgis-plugin-grass \
        qgis-providers \
        qgis 

#This avahi throws an error but is resolved with --bind-tcp=0.0.0.0:port in the xpra run
RUN apt-get install -y python3-pyinotify 

# Reduce the image size
RUN apt-get autoremove -y
RUN apt-get clean -y
RUN rm -rf /var/lib/apt/lists/*

RUN chmod u+s /usr/lib/libdlfaker.so

# change to QGIS user profile to remove any root access
WORKDIR /home/user/

# set display port #
ENV DISPLAY :100

USER user

CMD xpra start \
         --bind-tcp=0.0.0.0:9876 \
         --start-child=qgis \
         --exit-with-children=no \
         --html=on \
         --daemon=no \
         --xvfb="/usr/bin/Xvfb +extension Composite -screen 0 1920x1080x24+32 -nolisten tcp -noreset" \
         --pulseaudio=no \
         --notifications=no \
         --bell=no \
         :100
