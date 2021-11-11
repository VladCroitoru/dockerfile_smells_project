FROM rocker/tidyverse
MAINTAINER Steph Locke <steph@itsalocke.com>
RUN git clone https://github.com/lockedata/DOCKER-introR.git  && \
    cd DOCKER-introR/  && \
	cp sampleSQL.r /etc/skel/  && \
    apt-get update && \
    apt-get install -y libjpeg-dev apt-transport-https gnupg2 curl unixodbc && \
    chmod 777 ./mkusers.sh  && \
    ./mkusers.sh  && \
    chmod 777 ./odbcinstall.sh  && \
    ./odbcinstall.sh && \
    R -e 'devtools::install_deps()' 
