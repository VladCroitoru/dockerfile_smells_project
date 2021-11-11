# datelifedocker
# Version: 0.5.0

# First, you have to choose and get a shiny image.
# Specifying "latest" on version did not work (it kept loading a very old R version).
# I had to specify explicitly the R version number, i.e., rocker/shiny:latest -> rocker/shiny:4.1.0

# FROM rocker/shiny:latest
FROM rocker/shiny:4.1.0

MAINTAINER Luna Sare <sanchez.reyes.luna@gmail.com>

# Install Linux system libraries of general use

RUN apt-get update && apt-get -y dist-upgrade


RUN apt-get install -y apt-utils \
    software-properties-common \
    libssl-dev \
    libxml2-dev \
    lib32z1-dev \
    libblas-dev \
    liblapack-dev \
    libprotobuf-dev \
    protobuf-compiler \
    php libapache2-mod-php php-cli \
    git-core \
    curl \
    wget \
    libmagick++-dev libmagickcore-dev libmagickwand-dev \
    libssh2-1-dev \
    sudo \
    gdebi-core \
    pandoc \
    pandoc-citeproc \
    libcurl4-gnutls-dev \
    libcairo2-dev \
    libxt-dev \
    xtail \
    build-essential \
    libglpk40

RUN R -e "R.Version()"

# Initialize git lfs
# git lfs, from https://github.com/git-lfs/git-lfs/wiki/Installation and debugging the libssh2-1-dev install first.
RUN apt install -y libssh-4 libssh-dev libssh2-1 libssh2-1-dev

RUN apt-get update && \
    curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash && \
    apt-get install -y --no-install-recommends git-lfs && \
    git lfs install && \
    DEBIAN_FRONTEND=noninteractive apt-get purge -y --auto-remove ${build_deps} && \
    rm -r /var/lib/apt/lists/*

# Install packages needed for the datelife shiny app to run

RUN R -e "update.packages(ask=FALSE)"

RUN R -e "install.packages(c('igraph', 'ggdag'))"

RUN R -e "install.packages(c('rcmdcheck', \
    'shinycssloaders', \
    'strap', \
    'jsonlite', \
    'stringr', \
    'future', \
    'phangorn', \
    'latticeExtra', \
    'Hmisc'))"
RUN R -e "install.packages(c('shiny', \
    'shinydashboard', \
    'lubridate', \
    'magrittr', \
    'glue', \
    'DT', \
    'devtools', \
    'plotly'), repos='http://cran.rstudio.com/')"
RUN R -e "install.packages(c('bold', 'rotl', 'knitcitations', 'rentrez'), type='source')"
RUN R -e "devtools::install_github('fmichonneau/phylobase')"  # regular install.packages command not working with phylobase; tried type = "source" and did not work either
RUN R -e "devtools::install_github('fmichonneau/phyloch')"
RUN R -e "devtools::install_github('phylotastic/rphylotastic')"

# Installing datelife from GitHub
# you can install form a dev branch, for example:
# RUN R -e "devtools::install_github('phylotastic/datelife', ref = 'datelife-plots')"

RUN R -e "devtools::install_github('phylotastic/datelife')"


RUN R -e "devtools::install_github('phylotastic/datelifeplot')"

# Installing PATHd8

RUN mkdir /usr/local/pathd8download && \
  wget http://www2.math.su.se/PATHd8/PATHd8.zip -O /usr/local/pathd8download/PATHd8.zip && \
  cd /usr/local/pathd8download && \
  unzip /usr/local/pathd8download/PATHd8.zip && \
  cc PATHd8.c -O3 -lm -o PATHd8 && \
  cp PATHd8 /usr/local/bin/PATHd8

# Installing mrBayes

RUN apt-get update && \
    apt-get install -y mrbayes

# Copying the datelifeweb shiny app to the docker image so it can be served

RUN apt-get update && \
  cd /srv && \
  pwd && \
  rm -r /srv/shiny-server/* && \
  git clone https://github.com/phylotastic/datelifeweb.git && \
  mv /srv/datelifeweb/* /srv/shiny-server/



# select port
EXPOSE 80

CMD ["/usr/bin/shiny-server"]
