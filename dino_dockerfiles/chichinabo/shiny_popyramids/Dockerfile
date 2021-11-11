FROM r-base:latest

MAINTAINER Benito Zaragozí "benizar@gmail.com"

RUN apt-get update && apt-get install -y -t unstable \
    sudo \
    gdebi-core \
    pandoc \
    pandoc-citeproc \
    libcurl4-gnutls-dev \
    libcairo2-dev/unstable \
    libxt-dev \
    postgresql-server-dev-all

# Download and install shiny server
RUN wget --no-verbose https://s3.amazonaws.com/rstudio-shiny-server-os-build/ubuntu-12.04/x86_64/VERSION -O "version.txt" && \
    VERSION=$(cat version.txt)  && \
    wget --no-verbose "https://s3.amazonaws.com/rstudio-shiny-server-os-build/ubuntu-12.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb && \
    gdebi -n ss-latest.deb && \
    rm -f version.txt ss-latest.deb


RUN R -e "install.packages(c('shiny', 'rmarkdown', 'shinydashboard', 'leaflet', 'RJSONIO', 'epade', 'png', 'grid', 'RPostgreSQL'), repos='https://cran.rstudio.com/')"

COPY shiny-server.conf  /etc/shiny-server/shiny-server.conf
COPY /apps/ /srv/shiny-server/

EXPOSE 80

COPY shiny-server.sh /usr/bin/shiny-server.sh

CMD ["/usr/bin/shiny-server.sh"]
