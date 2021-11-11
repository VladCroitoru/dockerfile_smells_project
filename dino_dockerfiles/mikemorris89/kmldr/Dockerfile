FROM rocker/r-base

MAINTAINER mike morris "mike.morris89@github.com"

# system libraries of general use
RUN apt-get update  -qq \
 && apt-get upgrade -y

RUN apt-get install -y --no-install-recommends --allow-downgrades \
	apt-utils \
	default-jdk \
	libssl-dev \
	libxml2-dev \
	libcurl3-dev \
	libcurl4-openssl-dev \
	&& rm -rf /var/lib/apt/lists/*

RUN apt-get update -qq

RUN apt-get install -y wajig 
RUN wajig update 
RUN wajig install -y libgtk2.0-dev


# basic shiny functionality
RUN R -e "install.packages(c('devtools','roxygen2' ,'d3heatmap' ,'shinyjs' ,'AppliedPredictiveModeling' ,'caret' ,'pROC' ,'plotly' ,'ggplot2' ,'ggthemes' ,'scales' ,'dplyr' ,'mice' ,'randomForest' ,'shinydashboard' ,'reshape' ,'rpart' ,'htmlwidgets' ,'rattle' ,'rpart.plot' ,'RGtk2' ,'R6' ,'shinyBS' ,'RDocumentation' ,'titanic' ,'logging'),dep=T)" \
    && R -e 'devtools::install_github("mikemorris89/rmm")' \
    && R -e 'remove.packages("devtools")'


# copy the app to the image
RUN mkdir /root/kml
COPY kml /root/kml

COPY Rprofile.site /usr/lib/R/etc/

RUN mkdir /srv/shiny-server
RUN mkdir /srv/shiny-server/kml
VOLUME /srv/shiny-server/kml

EXPOSE 3838

CMD ["R", "-e shiny::runApp('/root/kml')"]

