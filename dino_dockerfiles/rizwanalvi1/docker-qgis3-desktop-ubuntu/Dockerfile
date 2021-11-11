FROM ubuntu:artful
MAINTAINER Rizwan Alvi <rizwan.alvi@tplmaps.com>

RUN    apt-get -y update

RUN    apt-get -y install dirmngr
RUN echo "deb http://qgis.org/debian-nightly artful main" >> /etc/apt/sources.list
RUN echo "deb-src http://qgis.org/debian-nightly artful main" >> /etc/apt/sources.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-key CAEB3DC3BDF7FB45

RUN    apt-get -y update

# For TauDEM
RUN    apt-get -y install libopenmpi-dev
RUN    apt-get -y install build-essential \
                          g++             \
                          wget            \
                          cmake

# Python
RUN    apt-get -y install python-requests   \
                          python-numpy      \
                          python-pandas     \
                          python-scipy      \
                          python-matplotlib \
                          python-pyside.qtwebkit

# QGIS
RUN    apt-get -y install libgdal-dev       \
                          gdal-bin          \
                          qgis              \
                          python-qgis       \
                          qgis-provider-grass \
                          grass

RUN    apt-get clean \
    && apt-get purge

# Download and build taudem
RUN wget -qO- https://api.github.com/repos/dtarb/TauDEM/tarball/master \
    | tar -xzC /usr/src \
    # Remove the TestSuite directory because it contains large files
    # that we don't need.
    && rm -rf /usr/src/dtarb-TauDEM-*/TestSuite \
    && cd /usr/src/dtarb-TauDEM-*/src \
    && rm -f Makefile makefile \
    && sed -i -e 's/OGR_F_GetFieldAsInteger64/OGR_F_GetFieldAsInteger/g' \
              -e 's/OFTInteger64/OFTInteger/g' ReadOutlets.cpp \
    && cmake . \ 
    && make \
    && make install
RUN rm -rf /usr/src/dtarb-TauDEM-*
ENV PATH /usr/local/bin:$PATH
ENV LD_LIBRARY_PATH /usr/local/lib:$LD_LIBRARY_PATH

# Called when the Docker image is started in the container
ADD start.sh /start.sh
RUN chmod 0755 /start.sh

CMD /start.sh