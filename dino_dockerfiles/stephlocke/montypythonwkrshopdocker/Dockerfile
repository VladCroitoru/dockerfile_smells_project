FROM rocker/tidyverse
MAINTAINER Steph Locke <steph@itsalocke.com>
RUN apt-get install libudunits2-0 libudunits2-dev whois
RUN  R -e 'devtools::install_github("lockedata/TextAnalysis")' 
RUN  R -e 'devtools::install_github("dgrtwo/widyr")' 
ADD https://gist.githubusercontent.com/stephlocke/0036331e7a3338e965149833e92c1360/raw/607fb01602e143671c83216a4c5f1ad2deb10bf6/mkusers.sh /
ADD https://gist.githubusercontent.com/stephlocke/0036331e7a3338e965149833e92c1360/raw/6d967c19d9c73cecd1e2d4da0eed2cd646790bd5/users.csv /
RUN chmod 777 /mkusers.sh
RUN /mkusers.sh