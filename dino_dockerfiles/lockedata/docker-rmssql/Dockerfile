FROM rocker/tidyverse
MAINTAINER Steph Locke <steph@itsalocke.com>
RUN git clone https://github.com/lockedata/DOCKER-rmssql.git  && \
    cd DOCKER-rmssql/  && \
	cp sampleSQL.r /etc/skel/  && \
    apt-get install -y apt-transport-https gnupg && \
    chmod 777 ./odbcinstall.sh  && \
    ./odbcinstall.sh && \
    R -e 'devtools::install_github("lockedata/DOCKER-rmssql")' 
