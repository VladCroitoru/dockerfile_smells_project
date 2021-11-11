FROM ubuntu:14.04
MAINTAINER Soroor Hediyeh Zadeh <hediyehzadeh.s@wehi.edu.au>
RUN echo "deb http://cran.ms.unimelb.edu.au/bin/linux/ubuntu trusty/" >> /etc/apt/sources.list   
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 
RUN apt-get update
RUN apt-get install -y software-properties-common libxml2-dev
RUN add-apt-repository ppa:marutter/rdev
RUN apt-get update  
RUN apt-get upgrade -y
RUN apt-get install -y -q r-base r-base-dev gdebi-core libapparmor1 supervisor wget git libcurl4-gnutls-dev
RUN (wget https://download2.rstudio.org/rstudio-server-1.0.136-amd64.deb && gdebi -n rstudio-server-1.0.136-amd64.deb)
RUN rm /rstudio-server-1.0.136-amd64.deb
RUN (adduser --disabled-password --gecos "" davislab && echo "davislab:davislab"|chpasswd)
RUN mkdir -p /var/log/supervisor
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN chown -R davislab:davislab /home/davislab
RUN chmod 700 /home/davislab
EXPOSE 8787
CMD ["/usr/bin/supervisord"]

