FROM rocker/geospatial:3.4.1

# Toolchain
RUN apt-get update \
    && apt-get -y install build-essential

# X11 Server Installation
# RUN apt-get -y install xorg openbox

# Configuration (personal Makevars file)
RUN mkdir -p $HOME/.R/ \
    && echo "\nCXXFLAGS=-O3 -mtune=native -march=native -Wno-unused-variable -Wno-unused-function\n" >> $HOME/.R/Makevars \
    && echo "\nCXXFLAGS+=-flto -ffat-lto-objects  -Wno-unused-local-typedefs\n" >> $HOME/.R/Makevars

# Installation
RUN install2.r --repo http://cloud.r-project.org/ --deps TRUE --error \
    rstan \
    leaflet \
    leaflet.extras \
    lme4 \
    ggthemes \
    showtext \
    tidyjson

# Text editor
RUN apt-get install nano

# Install pip (package manager)
RUN apt-get -y install python-pip

# Install Google APIs Client Library
RUN pip install google-api-python-client

# Install the Earth Engine Python API
RUN pip install earthengine-api

# Upgrade pyasn1 to resolve version conflict
RUN pip install pyasn1 --upgrade

# Install Pandas
RUN apt-get -y install python-pandas

# Hugo installation
RUN cd ~ \
    && wget https://github.com/spf13/hugo/releases/download/v0.20.7/hugo_0.20.7_Linux-64bit.deb \
    && dpkg -i hugo*.deb \
    && rm hugo*.deb

# ImageMagick
RUN wget https://www.imagemagick.org/download/ImageMagick.tar.gz -P /usr/local \
    && tar xvzf /usr/local/ImageMagick.tar.gz -C /usr/local/bin \
    && rm /usr/local/ImageMagick.tar.gz \
    && cd /usr/local/bin/ImageMagick-7.0.6-1 \
    && ./configure \
    && make \
    && make install \
    && ldconfig /usr/local/lib

# JAGS
RUN wget http://ftp.debian.org/debian/pool/main/j/jags/jags_4.3.0.orig.tar.gz -P /usr/local \
    && tar xvzf /usr/local/jags_4.3.0.orig.tar.gz -C /usr/local/bin \
    && rm /usr/local/jags_4.3.0.orig.tar.gz \
    && cd /usr/local/bin/JAGS-4.3.0 \
    && ./configure \
    && make \
    && make install

# Install additional R packages
RUN R -e "devtools::install_github('rstudio/blogdown')" \
    && R -e "devtools::install_github('adletaw/captioner')" \
    && R -e "devtools::install_github('ropensci/plotly')" \
    && R -e "devtools::install_github('haozhu233/kableExtra', ref='f200ce56bafab4dcfaaada294cd9d1b9599d2c68')" \
    && R -e "devtools::install_github('dgrtwo/gganimate')" \
    && R -e "install.packages('rjags', configure.args='--with-jags-include=/usr/local/include/JAGS --with-jags-lib=/usr/local/lib/JAGS --with-jags-modules=/usr/local/lib/JAGS/modules')"
