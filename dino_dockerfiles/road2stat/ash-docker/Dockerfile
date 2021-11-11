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

RUN git clone https://github.com/stephenslab/ash-packrat.git /home/rstudio/

# Basic R package dependencies for installing packrat
RUN Rscript -e "install.packages(c('RCurl', 'devtools'), repos = 'https://cran.rstudio.com')"

# Install packrat with liftr
RUN Rscript -e "source('https://cdn.rawgit.com/road2stat/liftrlib/fab41764ea8b56677d05c70c86225774164b6ca0/install_cran.R');install_cran(c('packrat/0.4.4'))"

# Install depended R packages with packrat
RUN Rscript -e "packrat::init('/home/rstudio/')"

# Set initial working directory
WORKDIR /home/rstudio/
