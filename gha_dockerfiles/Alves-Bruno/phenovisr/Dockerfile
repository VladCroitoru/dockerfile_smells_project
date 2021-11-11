FROM r-base:3.5.2

RUN apt-get update
RUN apt-get install -y libjpeg-dev libssl-dev libcurl4-openssl-dev

RUN echo 'install.packages("Rcpp")' | R --save
RUN echo 'install.packages("tidyverse")' | R --save

RUN mkdir /phenovisr
WORKDIR /phenovisr
COPY . /phenovisr

RUN R CMD INSTALL .

WORKDIR /