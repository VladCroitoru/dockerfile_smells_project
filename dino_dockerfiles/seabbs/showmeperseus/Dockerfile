
## Start with the shiny docker image
FROM rocker/tidyverse:3.4.3

MAINTAINER "Sam Abbott" contact@samabbott.co.uk

EXPOSE 3838

ADD . /home/rstudio/ShowMePerseus

RUN Rscript -e 'install.packages("packrat")'

WORKDIR /home/rstudio/ShowMePerseus

RUN Rscript -e 'packrat::restore()'

