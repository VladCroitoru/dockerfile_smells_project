#FROM rocker/tidyverse:3.5.2
FROM openanalytics/r-base
RUN apt-get -y update
RUN apt-get -y install libcurl4-openssl-dev
RUN apt-get -y install libssl-dev 
RUN apt-get -y install -y libxml2-dev
RUN R -e 'install.packages("remotes")'
RUN R -e 'remotes::install_github("r-lib/remotes", ref = "97bbf81")'
RUN R -e 'remotes::install_cran("cowplot")'
RUN R -e 'remotes::install_cran("DT")'
RUN R -e 'remotes::install_cran("ggplot2")'
RUN R -e 'remotes::install_cran("ggpubr")'
RUN R -e 'remotes::install_cran("nlme")'
RUN R -e 'remotes::install_cran("shiny")'
RUN R -e 'remotes::install_cran("tidyr")'
RUN R -e 'remotes::install_cran("covr")'
RUN R -e 'remotes::install_cran("testthat")'
RUN R -e 'remotes::install_cran("RSelenium")'
RUN R -e 'remotes::install_cran("Rlabkey")'
#RUN R -e 'remotes::install_cran("golem")'
RUN R -e 'install.packages("golem")'
COPY vici_*.tar.gz /app.tar.gz

RUN R -e 'remotes::install_local("/app.tar.gz")'

COPY Rprofile.site /usr/lib/R/etc/
# set host and port
EXPOSE 8080
#CMD  ["R", "-e","options('shiny.port'=3838,shiny.host='0.0.0.0'); vici::run_app()"]
CMD ["R", "-e", "vici::run_app()"]
