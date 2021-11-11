# We build our custom image from the existing rocker/tidyverse image which is an R install within an UBUNTU Linux.
FROM rocker/tidyverse:3.4.4

# provide information about the maintainer of the image
MAINTAINER Thomas Goossens (hello.pokyah@gmail.com)

# Download and install hugo blog to work with R blogdown
ENV HUGO_VERSION 0.33
ENV HUGO_BINARY hugo_${HUGO_VERSION}_Linux-64bit.deb
ADD https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY} /tmp/hugo.deb
RUN dpkg -i /tmp/hugo.deb \
	&& rm /tmp/hugo.deb

# We need to install all the UBUNTU dependencies required for our R-packages to work properly
RUN apt-get update \
    && apt-get install -y software-properties-common \
    && apt-get update -q \
    && apt-get install -y \
      texlive-full \
      jq \
      libjq-dev \
      libv8-3.14-dev \
      libprotobuf-dev \
      protobuf-compiler \
      libjq-dev \
      openssh-server \
      libxml2-dev \
      libssl-dev \
      libcurl4-openssl-dev \
      libgeos-dev \
      libcairo2-dev \
      libudunits2-dev \
      gdal-bin \
      libgdal-dev \
      libproj-dev \
      freeglut3 \
      freeglut3-dev \
      mesa-common-dev \
      default-jdk \
      r-cran-rjava \
      libmagick++-dev \
    && apt-get clean \ 
    && rm -rf /var/lib/apt/lists/ \ 
    && rm -rf /tmp/downloaded_packages/ /tmp/*.rds \
    && R CMD javareconf \
    && install2.r --error \
      rvest \
      pacman \
      lubridate \ 
      anytime \
      jsonlite \
      here \
      nortest \
      lazyeval \
      maptools \
      rmarkdown \
      knitr \
      maps \
      broom \
      stringr \
      RPostgreSQL \
      chron \
      readr \
      plotly \
      ggpubr \
      BlandAltmanLeh \
      sf \
      raster \
      scales \
      mapview \
      citr \
      gstat \
      spData \
      shiny \
      blogdown \
      RColorBrewer \
      revealjs \
      rJava \
      RWekajars \
      mlr \
      tmap \
   && rm -rf /tmp/downloaded_packages/ /tmp/*.rds \
   && rm -rf /var/lib/apt/lists/* \
   && installGithub.r Nowosad/spDataLarge \
   && installGithub.r r-lib/rlang \
   && installGithub.r tidyverse/ggplot2 \
   && rm -rf /tmp/downloaded_packages

