FROM buildpack-deps:xenial

RUN apt-get update && apt-get install -y \
  curl \
  supervisor \
  apt-transport-https

# install R
RUN apt-get install -y \
  r-base=3.2.* \
  libcurl4-openssl-dev \
  libnlopt-dev

# install julia
RUN apt-get install -y \
  software-properties-common \
  python-software-properties \
  && add-apt-repository -y ppa:staticfloat/juliareleases \
  && add-apt-repository -y ppa:staticfloat/julia-deps \
  && apt-get update && apt-get install -y \
  julia=0.5.* \
  libgmp3-dev \
  cmake \
  unzip \
  libhiredis-dev \
  hdf5-tools

COPY . /docker-statistics-image

# install R packages
RUN cd /docker-statistics-image && Rscript install_packages.R

# install julia packages
RUN cd /docker-statistics-image && julia install_packages.jl
