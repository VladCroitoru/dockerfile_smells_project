FROM nareal/r_docker_tidyverse_spiced

MAINTAINER "Nelson Areal" nareal@gmail.com

ENV DEBIAN-FRONTEND noninteractive  
ENV PATH /usr/lib/rstudio-server/bin/:$PATH   

RUN apt-get update -y \
  && apt-get --purge remove -y rstudio-server \
  && apt-get install -y libclang-dev \
  && wget --no-check-certificate \
    https://raw.githubusercontent.com/nareal/r_docker_tidyverse_spiced_preview/master/R/get_preview.R \
  && Rscript get_preview.R && rm get_preview.R 

RUN dpkg -i rstudio-server-preview-amd64.deb \
  && rm rstudio-server-*-amd64.deb   