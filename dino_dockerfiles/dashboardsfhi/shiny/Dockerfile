FROM r-base:latest

MAINTAINER Winston Chang "winston@rstudio.com"

RUN apt-get update && apt-get install -y -t unstable \
    sudo \
    gdebi-core \
    pandoc \
    pandoc-citeproc \
    libcurl4-gnutls-dev \
    libcairo2-dev/unstable \
    libxt-dev

RUN apt-get -y install libxml2-dev libssl-dev


# Download and install shiny server
RUN wget --no-verbose https://s3.amazonaws.com/rstudio-shiny-server-os-build/ubuntu-12.04/x86_64/VERSION -O "version.txt" && \
    VERSION=$(cat version.txt)  && \
    wget --no-verbose "https://s3.amazonaws.com/rstudio-shiny-server-os-build/ubuntu-12.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb && \
    gdebi -n ss-latest.deb && \
    rm -f version.txt ss-latest.deb && \
    R -e "install.packages(c('shiny', 'rmarkdown', 'ggvis', 'data.table', 'shinydashboard', 'flexdashboard', 'devtools', 'RCurl', 'readxl', 'plotly', 'DT', 'zoo', 'ggplot2'), repos='https://cran.rstudio.com/')" && \
    cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/

RUN R -e "devtools::install_github(c('cscheid/rgithub','dashboardsfhi/dashboardgraphs','bwlewis/doRedis'))"

RUN R -e "install.packages(c('ineq','ggrepel','htmlTable'), repos='https://cran.rstudio.com/')" 

EXPOSE 3838

COPY shiny-server.sh /usr/bin/shiny-server.sh
COPY shiny-server.conf /etc/shiny-server/shiny-server.conf

CMD ["/usr/bin/shiny-server.sh"]
