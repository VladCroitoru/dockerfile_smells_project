FROM r-base:latest

MAINTAINER Silvio de Morais "shirubio@gmail.com"

RUN apt-get update 

RUN apt-get -y upgrade

RUN apt-get -y autoremove

RUN apt-get install -y sudo
RUN apt-get install -y gdebi-core 
RUN apt-get install -y pandoc 
RUN apt-get install -y pandoc-citeproc 
RUN apt-get install -y libcurl4-gnutls-dev 

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

RUN R -e "install.packages(c('shiny', 'rmarkdown', 'tm', 'wordcloud', 'memoise', 'ggplot2', 'shinyBS'), repos='http://cran.rstudio.com/')"

COPY shiny-server.conf  /etc/shiny-server/shiny-server.conf
COPY /src/R /srv/shiny-server/
COPY /src/R/CSVs /srv/shiny-server/CSVs
COPY /src/R/CSVs/Illinois_GARS_Annual_Report_2014 /srv/shiny-server/CSVs/Illinois_GARS_Annual_Report_2014

EXPOSE 80

COPY shiny-server.sh /usr/bin/shiny-server.sh

CMD ["/usr/bin/shiny-server.sh"]

