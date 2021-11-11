FROM r-base:latest

MAINTAINER Winston Chang "winston@rstudio.com"

RUN apt-get update -qq && \
    apt-get install -y -t unstable --no-install-recommends \
        aptitude \
        git \
        sudo \
        gdebi-core \
        pandoc \
        pandoc-citeproc \
        libcurl4-gnutls-dev \
        libcairo2-dev/unstable \
        libxt-dev

RUN aptitude install -y \
    libgdal-dev \
    libproj-dev

# Download and install libssl 0.9.8
RUN wget --no-verbose http://ftp.us.debian.org/debian/pool/main/o/openssl/libssl0.9.8_0.9.8o-4squeeze14_amd64.deb && \
    dpkg -i libssl0.9.8_0.9.8o-4squeeze14_amd64.deb && \
    rm -f libssl0.9.8_0.9.8o-4squeeze14_amd64.deb

# Download and install shiny server
RUN wget --no-verbose https://s3.amazonaws.com/rstudio-shiny-server-os-build/ubuntu-12.04/x86_64/VERSION -O "version.txt" && \
    VERSION=$(cat version.txt)  && \
    wget --no-verbose "https://s3.amazonaws.com/rstudio-shiny-server-os-build/ubuntu-12.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb && \
    gdebi -n ss-latest.deb && \
    rm -f version.txt ss-latest.deb

RUN R -e "install.packages(c('bitops','caTools','colorspace','curl','devtools','dplyr','ggplot2','httr','Hmisc','knitr','lubridate','markdown','qcc','RColorBrewer','RCurl','reshape','rgdal','rjson','scales','shiny','shinyIncubator','stringr','tidyr','tm','whisker','wordcloud'), repos='https://cran.rstudio.com/')"

RUN R -e "devtools::install_github('ropensci/ckanr')"

RUN R -e "ckanr::ckanr_setup(url='http://data.nrgi-rad.org/')"

RUN cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/

EXPOSE 3838

COPY shiny-server.sh /usr/bin/shiny-server.sh

CMD ["/usr/bin/shiny-server.sh"]