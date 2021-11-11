FROM openanalytics/r-base

MAINTAINER Mikkel Freltoft Krogsholm "mikkel@56n.dk"

# system libraries of general use
RUN apt-get update && apt-get install -y \
    sudo \
    pandoc \
    pandoc-citeproc \
    libcurl4-gnutls-dev \
    libcairo2-dev \
    libxt-dev \
    libssl-dev \
    libssh2-1-dev \
    libssl1.0.0 \
    libxml2-dev \
    libcurl4-gnutls-dev \
    libv8-3.14-dev

# Install java
RUN apt-get update && apt-get install -y \
  default-jdk \
  && R CMD javareconf \
  && apt-get install -y r-cran-rjava

# Install basic shiny functionality and the tidyverse
RUN R -e "install.packages(c('shiny', 'rmarkdown', 'shinydashboard', 'tidyverse'), repos = 'https://cloud.r-project.org/')"

COPY Rprofile.site /usr/lib/R/etc/

EXPOSE 3838

CMD ["R", "-e", "shiny::runApp('/app')"]
