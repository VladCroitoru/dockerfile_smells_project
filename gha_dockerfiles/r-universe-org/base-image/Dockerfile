FROM ubuntu:focal

ENV DEBIAN_FRONTEND noninteractive

RUN \
    apt-get update && \
    apt-get -y dist-upgrade && \
    apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:marutter/rrutter4.0 && \
    add-apt-repository -y "ppa:c2d4u.team/c2d4u4.0+" && \
    apt-get update && \
    apt-get install -y git wget curl pandoc pandoc-citeproc r-base-dev libcurl4-gnutls-dev libssl-dev \
    libgdal-dev libgeos-dev libproj-dev libopencv-dev libtesseract-dev tesseract-ocr-eng libmagick++-dev \
    libprotoc-dev libprotobuf-dev protobuf-compiler libgit2-dev libxml2-dev libxslt-dev libudunits2-dev \
    libpoppler-cpp-dev libsodium-dev libjq-dev libicu-dev libavfilter-dev cargo libv8-dev libmysqlclient-dev \
    unixodbc-dev libpq-dev language-pack-en-base libgpgme-dev libdb-dev libcairo2-dev coinor-libcbc-dev  \
    libfftw3-dev libfreetype6-dev libhdf5-dev libhiredis-dev libarchive-dev libjpeg-dev libpng-dev librsvg2-dev \
    libsecret-1-dev libsodium-dev libssh-dev libssh2-1-dev libtiff-dev libwebp-dev libnetcdf-dev libsasl2-dev \
    libzmq3-dev zlib1g-dev libglpk-dev librdf0-dev libglu1-mesa-dev libgsl-dev libharfbuzz-dev libfribidi-dev \
    coinor-libsymphony-dev libapparmor-dev libelf-dev libmpfr-dev libboost-program-options-dev librrd-dev \
    r-cran-rjava jags hugo ttf-mscorefonts-installer fonts-emojione texinfo cmake python3-numpy global && \
    apt-get clean

COPY Renviron /etc/R/Renviron.site
COPY Rprofile /etc/R/Rprofile.site

# NB: Docker says $HOME should be available but it isnt so we hardcode /root for now
ENV PATH="/root/bin:${PATH}"

# Install TinyTex + common packages and put it on the PATH
RUN R -e 'install.packages("tinytex");tinytex:::install_prebuilt("TinyTeX")' && \
    rm -f TinyTeX.tar.gz && \
    tlmgr option repository https://ctan.math.illinois.edu/systems/texlive/tlnet
