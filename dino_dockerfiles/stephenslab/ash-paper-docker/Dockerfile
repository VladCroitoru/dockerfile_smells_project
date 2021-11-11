FROM rocker/rstudio:latest
MAINTAINER Nan Xiao <nanx@uchicago.edu>

# System dependencies for required R packages
RUN  rm -f /var/lib/dpkg/available \
  && rm -rf  /var/cache/apt/* \
  && apt-get update -qq \
  && apt-get install -t unstable -y --no-install-recommends \
    libxml2-dev \
    libssh2-1-dev

# TeXLive + Inconsolata font from rocker/hadleyverse
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    aspell \
    aspell-en \
    ghostscript \
    imagemagick \
    lmodern \
    texlive-fonts-recommended \
    texlive-humanities \
    texlive-latex-extra \
    texinfo \
  && apt-get clean \
  && cd /usr/share/texlive/texmf-dist \
  && wget http://mirrors.ctan.org/install/fonts/inconsolata.tds.zip \
  && unzip inconsolata.tds.zip \
  && rm inconsolata.tds.zip \
  && echo "Map zi4.map" >> /usr/share/texlive/texmf-dist/web2c/updmap.cfg \
  && mktexlsr \
  && updmap-sys

# Install packrat v0.4.4
RUN Rscript -e "install.packages('http://cran.rstudio.com/src/contrib/Archive/packrat/packrat_0.4.4.tar.gz')"

# Clone the stephenslab/ash repo with accurate branch and commit
RUN git clone -b master --single-branch https://github.com/stephenslab/ash.git /home/rstudio/ && cd /home/rstudio/ && git reset --hard eb2dc55af17e5b79a804e204753795396b3fa4fe

# Install depended R packages with packrat
RUN Rscript -e "packrat::init('/home/rstudio/')"

# Set initial working directory
WORKDIR /home/rstudio/
