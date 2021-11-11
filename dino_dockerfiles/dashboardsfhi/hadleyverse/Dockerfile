FROM rocker/hadleyverse
MAINTAINER "Carl Boettiger and Dirk Eddelbuettel" rocker-maintainers@eddelbuettel.com

RUN R -e "install.packages(c('ggrepel','lme4','arm'))"
# deSolve

RUN R -e "devtools::install_github(c('raubreywhite/RAWmisc','dashboardsfhi/dashboardgraphs','bwlewis/doRedis'))"
RUN apt-get update \
  && apt-get install -y sshpass
