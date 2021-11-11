FROM ubuntu:14.04
MAINTAINER Somebody <somebody@acme.com>
ENV DEBIAN_FRONTEND noninteractive
ENV HOME /root
RUN apt-get update
RUN apt-get install -y --force-yes --no-install-recommends software-properties-common apt-transport-https
RUN add-apt-repository -y 'deb https://cran.rstudio.com/bin/linux/ubuntu/ trusty/'
RUN apt-get -y update --allow-unauthenticated
RUN apt-get install -y --force-yes --no-install-recommends apt-transport-https r-base-dev r-base bwa python-numpy
#rnaseq_dtoxs.json
#r.json
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 
#--
#bwa.json
#--
add lib/rnaseq_dtoxs/deps.R /tmp/deps.R
RUN Rscript /tmp/deps.R 
RUN rm /tmp/deps.R 
copy lib/rnaseq_dtoxs/LINCS.tar.gz /root/LINCS.tar.gz
RUN cd /root/ && tar -xf LINCS.tar.gz 
#--
RUN apt-get purge -y --force-yes r-base-dev
RUN apt-get purge software-properties-common -y --force-yes
RUN apt-get -y autoclean
RUN apt-get -y autoremove
RUN rm -rf /var/lib/apt/lists/*
RUN rm -rf /tmp/*
RUN rm -rf /var/tmp/*
# RUN bash -c 'echo -e "#!/bin/bash" >> /entrypoint.sh'
# RUN chmod +x /entrypoint.sh
# ENTRYPOINT ["/entrypoint.sh"]
CMD ["/bin/bash"]