FROM akzaidi/mrclient-rstudio
MAINTAINER Steph Locke <steph@itsalocke.com>
RUN git clone https://github.com/lockedata/docker-intromicrosoftr  && \
    cd docker-intromicrosoftr/  && \
	cp sampleSQL.r /etc/skel/  && \
    apt-get install -y apt-transport-https gnupg && \
    chmod 777 ./odbcinstall.sh  && \
    ./odbcinstall.sh && \
	R -e 'install.packages("devtools",repos = "https://cran.rstudio.com")' &&\
    R -e 'devtools::install_github("lockedata/docker-intromicrosoftr")' 
