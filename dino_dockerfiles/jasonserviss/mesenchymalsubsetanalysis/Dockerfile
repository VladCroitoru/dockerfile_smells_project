FROM rocker/tidyverse:3.4.1

MAINTAINER Jason Serviss <jason.serviss@ki.se>

# System dependencies for required R packages
RUN  rm -f /var/lib/dpkg/available \
  && rm -rf  /var/cache/apt/* \
  && apt-get update -qq \
  && apt-get install -y --no-install-recommends \
    ca-certificates \
    libssl-dev \
    libcurl4-openssl-dev \
    libxml2-dev \
    git

RUN Rscript -e "install.packages(c('devtools','knitr','rmarkdown','shiny','RCurl'), repos = 'https://cran.rstudio.com')"

RUN Rscript -e "source('https://cdn.rawgit.com/road2stat/liftrlib/aa132a2d/install_cran.R');install_cran(c('mclust/5.3','printr/0.1','ggthemes/3.4.0','viridis/0.4.0','viridisLite/0.2.0', 'purrr/0.2.4'))"

# Clone and install mesenchymalSubsetAnalysis package
RUN git clone https://github.com/jasonserviss/mesenchymalSubsetAnalysis.git /home/mesenchymalSubsetAnalysis
RUN Rscript -e "devtools::install('/home/mesenchymalSubsetAnalysis')"

WORKDIR /home/mesenchymalSubsetAnalysis


