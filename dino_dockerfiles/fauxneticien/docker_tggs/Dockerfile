FROM rocker/tidyverse

RUN apt-get update && apt-get install -y libv8-dev rclone && \
    Rscript -e 'devtools::install_github("fauxneticien/phonpack")' && \
    Rscript -e 'install.packages("googlesheets")'

ADD run.R /
