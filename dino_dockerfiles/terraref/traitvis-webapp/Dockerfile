FROM rocker/shiny

MAINTAINER "Nicholas Heyek and David LeBauer"

ENV bety_dbname=bety
ENV bety_password=bety
ENV bety_host=localhost
ENV bety_user=bety
ENV bety_port=5432

RUN apt-get update -qq \
         && apt-get -y install --no-install-recommends \
         cron \
         libgeos-dev \
         libpq-dev \
         libcurl4-openssl-dev \
         libssl-dev \
         libxml2-dev

RUN install2.r --error \
         cronR \
         dbplyr \
         dplyr \
         ggplot2 \
         leaflet \
         lubridate \
         shiny \
         shinythemes \
         rgeos \
         RPostgreSQL \
         timevis \
         kableExtra \
         heritability \
      && rm -rf /srv/shiny-server/sample-apps

RUN apt-get update \
    && apt-get install -y \
        libudunits2-dev \
        libgdal-dev \
        gdal-bin \
    && install2.r --error \
         mapview

RUN install2.r --error \
         sf

RUN wget https://cran.r-project.org/src/contrib/leafem_0.0.1.tar.gz \
    && R CMD INSTALL leafem_0.0.1.tar.gz

RUN install2.r --error rgdal

COPY . /srv/shiny-server/
COPY shiny-server.conf /etc/shiny-server/
RUN chown -R shiny:shiny /srv/shiny-server && \
    chown -R shiny:shiny /var/lib/shiny-server
USER shiny

ENTRYPOINT ["/srv/shiny-server/entrypoint.sh"]
