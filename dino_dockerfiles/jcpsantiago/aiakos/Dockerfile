FROM crukcibioinformatics/shiny-base

MAINTAINER Joao Santiago

RUN R -e 'install.packages("RSQLite", repos = "https://cloud.r-project.org")'
RUN R -e 'install.packages("dbplyr", repos = "https://cloud.r-project.org")'
RUN R -e 'install.packages("highcharter", repos = "https://cloud.r-project.org")'
RUN R -e 'install.packages("shinythemes", repos = "https://cloud.r-project.org")'
RUN R -e 'install.packages("shinyjs", repos = "https://cloud.r-project.org")'
RUN R -e 'install.packages("pool", repos = "https://cloud.r-project.org")'
RUN R -e 'install.packages("DT", repos = "https://cloud.r-project.org")'
RUN R -e 'install.packages("devtools", repos = "https://cloud.r-project.org")'
RUN R -e "devtools::install_github('hadley/emo')"
RUN R -e "devtools::install_github('tidyverse/glue')"
RUN R -e "devtools::install_github('ThomasSiegmund/shinyTypeahead')"

# install latest development version of DT from github
# stable release v0.2 has ajax error issue (https://github.com/rstudio/DT/issues/266)
# note that one of the dependencies of the devtools package (httr) requires curl and openssl
RUN R -e 'install.packages("devtools", repos = "https://cloud.r-project.org")'
RUN R -e 'devtools::install_github("rstudio/DT")'

RUN mkdir /srv/shiny-server/Aiakos/

RUN mkdir /srv/shiny-server/Aiakos/DB

RUN chmod -R a+rwx /srv/shiny-server/Aiakos/

ADD www	/srv/shiny-server/Aiakos/www
COPY *.R /srv/shiny-server/Aiakos/
