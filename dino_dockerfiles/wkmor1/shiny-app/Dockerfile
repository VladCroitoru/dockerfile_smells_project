FROM ubuntu
MAINTAINER William K Morris <wkmor1@gmail.com>

# Install Ubuntu packages
RUN    apt-get update \
    && apt-get install -y --no-install-recommends \
         curl \
         gdebi-core \
         locales

# Set locale
ENV    LANG     en_US.UTF-8
ENV    LANGUAGE $LANG
RUN    echo "en_US "$LANG" UTF-8" >> /etc/locale.gen \
    && locale-gen en_US $LANG \
    && update-locale LANG=$LANG LANGUAGE=$LANG

# Install R
RUN     echo "deb http://ppa.launchpad.net/marutter/rrutter/ubuntu trusty main" >> /etc/apt/sources.list \
    &&  gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys B04C661B \
    &&  gpg -a --export B04C661B | apt-key add - \
    &&  apt-get update \
    &&  apt-get install -y --no-install-recommends r-base-dev \
    &&  echo "options(repos = c(CRAN = 'https://cran.rstudio.com/'), download.file.method = 'libcurl')" >> /etc/R/Rprofile.site

# Install Shiny
RUN    mkdir -p var/log/shiny-server \
    && SHINYVER=$(curl https://s3.amazonaws.com/rstudio-shiny-server-os-build/ubuntu-12.04/x86_64/VERSION) \
    && curl -o shiny.deb https://s3.amazonaws.com/rstudio-shiny-server-os-build/ubuntu-12.04/x86_64/shiny-server-$SHINYVER-amd64.deb \
    && gdebi -n shiny.deb \
    && R -e "install.packages('shiny')"

# Clean up
RUN    apt-get clean \
    && apt-get autoremove \
    && rm -rf \
         var/lib/apt/lists/* \
         srv/shiny-server/* \
         shiny.deb

COPY shiny-server.sh usr/bin/shiny-server.sh

EXPOSE 3838

CMD ["/usr/bin/shiny-server.sh"]
