## Start with the tidyverse docker image
FROM rocker/tidyverse:latest

MAINTAINER "Sam Abbott" contact@samabbott.co.uk

ADD . /home/rstudio/TB_England_Wales

EXPOSE 3838

RUN Rscript -e 'install.packages("shiny")'

RUN Rscript -e 'devtools::install_github("rstudio/flexdashboard")'

RUN Rscript -e 'devtools::install_github("seabbs/tbinenglanddataclean")'

RUN Rscript -e 'install.packages("DT")'

RUN Rscript -e 'devtools::install_github("ropensci/plotly")' 
