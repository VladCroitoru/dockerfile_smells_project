## Emacs, make this -*- mode: sh; -*-

## Modified from rocker/shiny -- for florida plankton shiny app

FROM r-base:latest

MAINTAINER Francois Michonneau "francois.michonneau@gmail.com"

RUN apt-get update && apt-get dist-upgrade -y && apt-get install -y -t unstable \
    sudo \
    gdebi-core \
    pandoc \
    pandoc-citeproc \
    libcurl4-gnutls-dev \
    libcairo2-dev/unstable \
    libxt-dev \
    libssl-dev \
    libssh2-1-dev \
    libxml2-dev

# Download and install shiny server
RUN wget --no-verbose https://s3.amazonaws.com/rstudio-shiny-server-os-build/ubuntu-12.04/x86_64/VERSION -O "version.txt" && \
    VERSION=$(cat version.txt)  && \
    wget --no-verbose "https://s3.amazonaws.com/rstudio-shiny-server-os-build/ubuntu-12.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb && \
    gdebi -n ss-latest.deb && \
    rm -f version.txt ss-latest.deb

RUN R -e "install.packages(c('rmarkdown', 'leaflet', 'shiny', 'devtools'), repos='https://cran.rstudio.com/'); devtools::install_github('rstudio/shiny'); devtools::install_github('fmichonneau/chopper'); devtools::install_github('fmichonneau/labmanager')"

RUN cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/

EXPOSE 3838

COPY shiny-server.sh /usr/bin/shiny-server.sh

RUN chmod +x /usr/bin/shiny-server.sh

CMD ["/usr/bin/shiny-server.sh"]
