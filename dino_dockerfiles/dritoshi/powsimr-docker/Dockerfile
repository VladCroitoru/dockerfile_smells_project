FROM ubuntu:16.04

MAINTAINER Itoshi NIKAIDO <dritoshi@gmail.com>

ARG DEBIAN_FRONTEND=noninteractive

# Install R
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y apt-transport-https  && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 && \
    echo "\ndeb https://cran.ism.ac.jp/bin/linux/ubuntu xenial/" >> /etc/apt/sources.list && \
    echo "deb-src https://cran.ism.ac.jp/bin/linux/ubuntu xenial/" >> /etc/apt/sources.list && \
    apt-get update && apt-get upgrade && \
    apt-get install -y build-essential && \
    apt-get install -y software-properties-common && \
    apt-get install -y curl git man unzip wget xserver-xorg xserver-xorg-dev && \
    apt-get install -y libcairo2-dev libxml2-dev libssl-dev libcurl4-openssl-dev imagemagick && \
    apt-get install -y keyboard-configuration libmariadb-client-lgpl-dev libpq-dev libxt-dev libcairo2-dev && \
    apt-get install -y libglu1-mesa-dev freeglut3-dev mesa-common-dev libnetcdf-dev libglpk-dev && \
    apt-get install -y coinor-symphony coinor-libsymphony-dev cdbs coinor-libcgl-dev autotools-dev coinor-libsymphony3 && \
    apt-get install -y libopenmpi-dev && \
    apt-get install -y r-base r-base-dev && \
    apt-get install -y r-cran-rsymphony r-cran-rgl r-cran-rglpk r-cran-runit

# Setup R
ADD .Renviron $PWD

# Install PowsimR
ADD install_powsimR.R /tmp
RUN R -f /tmp/install_powsimR.R
