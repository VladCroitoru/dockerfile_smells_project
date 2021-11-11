## Start with the tidyverse docker image
FROM rocker/tidyverse:latest

MAINTAINER "Sam Abbott" contact@samabbott.co.uk

ADD . /home/rstudio/tbinenglanddataclean

RUN Rscript -e 'devtools::install_deps("/home/rstudio/tbinenglanddataclean", dependencies = TRUE)'

RUN Rscript -e 'devtools::install_github("hadley/pkgdown")'

RUN Rscript -e 'install.packages("caTools")'