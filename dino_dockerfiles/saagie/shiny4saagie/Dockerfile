FROM cardcorp/r-java

MAINTAINER aurele@saagie.com

RUN apt-get update && apt-get install -y -t unstable \
    sudo \
    gdebi-core \
    pandoc \
    pandoc-citeproc \
    libcurl4-gnutls-dev \
    libcairo2-dev/unstable \
    libxt-dev \
    curl \
    openssl
    
RUN mkdir /usr/lib/impala && mkdir /usr/lib/impala/lib && cd /usr/lib/impala/lib && \
    curl -O https://downloads.cloudera.com/impala-jdbc/impala-jdbc-0.5-2.zip && \
    unzip -j impala-jdbc-0.5-2.zip && rm impala-jdbc-0.5-2.zip

RUN R -e 'install.packages(c("RJDBC", "RImpala"), repos = "http://cran.rstudio.com")'

RUN wget --no-verbose https://s3.amazonaws.com/rstudio-shiny-server-os-build/ubuntu-12.04/x86_64/VERSION -O "version.txt" && \
    VERSION=$(cat version.txt)  && \
    wget --no-verbose "https://s3.amazonaws.com/rstudio-shiny-server-os-build/ubuntu-12.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb && \
    gdebi -n ss-latest.deb && \
    rm -f version.txt ss-latest.deb && \
    R -e "install.packages(c('shiny', 'rmarkdown'), repos='https://cran.rstudio.com/')" && \
    cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/

EXPOSE 3838

COPY shiny-server.sh /usr/bin/shiny-server.sh

RUN chmod 755 /usr/bin/shiny-server.sh

# Hacky way to display the app located at /srv/shiny-server/myapp in iframe
COPY index.html /srv/shiny-server/index.html

