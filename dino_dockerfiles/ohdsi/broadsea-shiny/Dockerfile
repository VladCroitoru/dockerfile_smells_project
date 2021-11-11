FROM rocker/shiny:4.1.0

MAINTAINER Lee Evans - www.ltscomputingllc.com

RUN apt-get update && apt-get install -y \
    openjdk-8-jdk liblzma-dev libbz2-dev libicu-dev libssl-dev libxml2-dev \
    texlive-science texlive-fonts-recommended texlive-fonts-extra texlive-latex-extra \
    libtiff-dev libjpeg-dev \
    && R CMD javareconf

RUN R -e "install.packages( \
 c( \
  'openssl', \
  'httr', \
  'plotly', \
  'shinycssloaders', \
  'rJava', \
  'SqlRender', \
  'shinydashboard', \
  'DT', \
  'pROC', \
  'DatabaseConnector', \
  'EmpiricalCalibration', \
  'ggplot2', \
  'shinyWidgets', \
  'visNetwork', \
  'shinyjs', \
  'shinyFiles', \
  'auth0', \
  'rhandsontable', \
  'shinyBS', \
  'shinythemes', \
  'rlist', \
  'uuid', \
  'VennDiagram', \
  'zeallot', \
  'reshape2', \
  'readr', \
  'aws.s3', \
  'aws.ec2metadata', \
  'shiny.i18n', \
  'pool', \
  'reshape', \
  'ggiraph', \
  'checkmate', \
  'purrr', \
  'RJSONIO', \
  'diffr', \
  'remotes', \
  'future', \
  'UpSetR' \
 ), \
 repos='http://cran.rstudio.com/' \
) "

RUN R -e "install.packages(pkgs = 'https://cran.r-project.org/src/contrib/Archive/googledrive/googledrive_0.1.3.tar.gz') "

RUN R -e "install.packages( \
 c( \
  'ggrepel', \
  'epitools', \
  'extrafont', \
  'cowplot', \
  'jpeg', \
  'survminer' \
 ), \
 repos='http://cran.rstudio.com/' \
) "

RUN R -e "remotes::install_github('OHDSI/CirceR')" && \
    R -e "remotes::install_github('OHDSI/Capr', upgrade='always')"

RUN R -e "remotes::install_github('OHDSI/ROhdsiWebApi', upgrade='always')" && \
    R -e "remotes::install_github('OHDSI/CohortDiagnostics', upgrade='always')"

RUN R -e "install.packages( \
 c( \
  'tsibble', \
  'feasts', \
  'fable' \
 ), \
 repos='http://cran.rstudio.com/' \
) "
