FROM r-base:latest

MAINTAINER Flavio Barros "flaviommbarros@gmail.com"

RUN apt-get update && apt-get install -y \
    sudo \
    gdebi-core \
    pandoc \
    pandoc-citeproc \
    libcurl4-gnutls-dev \
    libcairo2-dev/unstable \
    libxt-dev \
    libssl-dev \
    libxml2-dev \
    libnss-wrapper \
    gettext

# Download and install shiny server
RUN wget --no-verbose https://s3.amazonaws.com/rstudio-shiny-server-os-build/ubuntu-12.04/x86_64/VERSION -O "version.txt" && \
    VERSION=$(cat version.txt)  && \
    wget --no-verbose "https://s3.amazonaws.com/rstudio-shiny-server-os-build/ubuntu-12.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb && \
    gdebi -n ss-latest.deb && \
    rm -f version.txt ss-latest.deb

RUN R -e "install.packages(c('shiny', 'rmarkdown', 'tidyverse', 'ggplot2', 'deSolve', 'remotes'), repos='http://cran.rstudio.com/')"

RUN chown -R 1001:0 /srv/shiny-server && \
    chmod -R ug+rwx /srv/shiny-server && \
    mkdir -p /var/log/shiny-server && \
    chown -R 1001:0 /var/log/shiny-server && \
    chmod -R ug+rwx /var/log/shiny-server && \
    mkdir -p /var/lib/shiny-server/bookmarks && \
    chown -R 1001:0 /var/lib/shiny-server/bookmarks && \
    chmod -R ug+rwx /var/lib/shiny-server/bookmarks && \
    touch /tmp/passwd && \
    chmod 664 /tmp/passwd

# Set associated nss_wrapper environment variables.
ENV LD_PRELOAD=/usr/lib/libnss_wrapper.so
ENV NSS_WRAPPER_PASSWD=/tmp/passwd
ENV NSS_WRAPPER_GROUP=/etc/group

COPY shiny-server.conf  /etc/shiny-server/shiny-server.conf
COPY /myapp /srv/shiny-server/
COPY passwd.template /tmp/passwd.template

EXPOSE 8080

COPY shiny-server.sh /usr/bin/shiny-server.sh
USER 1001
CMD ["/usr/bin/shiny-server.sh"]
