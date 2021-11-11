FROM rocker/tidyverse
MAINTAINER Steph Locke <steph@itsalocke.com>
RUN git clone https://github.com/lockedata/DOCKER-BODS.git  && \
    cd DOCKER-BODS/  && \
	cp brentsbiz/* /etc/skel/  && \
    apt-get install -y libjpeg-dev apt-transport-https gnupg && \
    chmod 777 ./mkusers.sh  && \
    ./mkusers.sh  && \
    chmod 777 ./odbcinstall.sh  && \
    ./odbcinstall.sh && \
    R -e 'devtools::install_github("lockedata/DOCKER-bods")' 
